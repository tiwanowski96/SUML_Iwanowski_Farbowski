import csv
import os
import pickle
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from pyexpat import model

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

from ..forms import DiabeticPredictionForm
from ..models import Diabetes


class DiabeticTrainView(View):
    '''Train diabetic model view'''
    def get(self, request):
        '''prepare data for the view'''
        if not Diabetes.objects.exists():
            return render(request, 'diviner/model_empty.html')

        self.export_csv(self)

        X_train, X_test, y_train, y_test = self.trainModel(self)
        forest, lreg, tree = self.model(self, X_train, y_train)

        y1_predict = forest.predict(X_test)
        y2_predict = lreg.predict(X_test)
        y3_predict = tree.predict(X_test)

        y1_score = accuracy_score(y_test, y1_predict)
        y2_score = accuracy_score(y_test, y2_predict)
        y3_score = accuracy_score(y_test, y3_predict)

        choices = [y1_score, y2_score, y3_score]
        choice = max(choices)

        if choice == y1_score:
            model = forest
        elif choice == y2_score:
            model = lreg
        else:
            model = tree

        try:
            f = open("model.sv")
            os.remove("model.sv")
        except IOError:
            print("File not accessible")
        
        filename = "model.sv"
        pickle.dump(model, open(filename,'wb'))

        ctx = {
            'forest': "Las: {0}".format(forest.score(X_train,y_train)),
            'lreg': "Regresja logistyczna: {0}".format(lreg.score(X_train,y_train)),
            'tree': "Drzewa decyzyjne: {0}".format(tree.score(X_train,y_train)),
            'y1_predict': "Random Forest {0}".format(y1_score),
            'y2_predict': "Logistic Regresion {0}".format(y2_score),
            'y3_predict': "Decision Tree {0}".format(y3_score),
        }
        return render(request, 'diviner/train.html', ctx)


    def export_csv(self, request):
        '''create csv file of diabetes data'''
        diabetes = Diabetes.objects.all()

        try:
            f = open("diabetes.csv")
            os.remove("diabetes.csv")
        except IOError:
            print("File not accessible")

        csv_file = open('diabetes.csv', 'w')
        writer = csv.writer(csv_file)
        writer.writerow(["id", "sick","sex","age","high_blood_preasure","cholesterol","bmi","smoker","stroke","heart_disease_or_attack",
                "physical_activity","heavy_alcohol_consumption","healthcare","general_health_feeling","mental_health_feeling",
                "physical_health_feeling","education"])
        diabet = diabetes.values_list("id", "sick","sex","age","high_blood_preasure","cholesterol","bmi","smoker","stroke","heart_disease_or_attack",
                "physical_activity","heavy_alcohol_consumption","healthcare","general_health_feeling","mental_health_feeling",
                "physical_health_feeling","education")
        for row in diabet:
            writer.writerow(row)
        return csv_file


    def trainModel(self, request):
        '''train diabetics model'''
        all_entries = pd.read_csv('diabetes.csv')
        all_entries.columns
        cols = ["sick","sex","age","high_blood_preasure","cholesterol","bmi","smoker","stroke","heart_disease_or_attack",
                "physical_activity","heavy_alcohol_consumption","healthcare","general_health_feeling","mental_health_feeling",
                "physical_health_feeling","education"]
        data = all_entries[cols].copy()
        data.isnull().any()
        y = data.iloc[:,0] #  - zmienna, którą będziemy chcieli przewidzieć
        print(f'y: {y}')
        x = data.iloc[:,1:16] # zmienne na podstawie, których chcemy przewidzieć
        print(f'x: {x}')
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
        return X_train, X_test, y_train, y_test


    def model(self, request, X_train, y_train):
        '''return diabetics models'''
        forest = RandomForestClassifier( n_estimators=10, random_state=0)
        forest.fit(X_train,y_train)
        # print("Las: {0}".format(forest.score(X_train,y_train)) )
        
        lreg = LogisticRegression()
        lreg.fit(X_train,y_train)
        # print("Regresja logistyczna: {0}".format(lreg.score(X_train,y_train)) )
    
        tree = DecisionTreeClassifier()
        tree.fit(X_train,y_train)
        # print("Drzewa decyzyjne: {0}".format(tree.score(X_train,y_train)) )

        return forest, lreg, tree
