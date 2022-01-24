from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import View
from ..forms import DiabeticPredictionForm
from ..models import Diabetes

import pandas as pd
import numpy as np
import matplotlib as plt
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


class DiabeticTrainView(View):
    def get(self, request):
        result=self.hello(self)
        ctx={'result': result}
        return render(request, 'diviner/train.html', ctx)
    def  trainModel():
        all_entries = Diabetes.objects.all()
        all_entries.columns  
        cols = ["sick","sex","age","high_blood_preasure","cholesterol","bmi","smoker","stroke","heart_disease_or_attack",
                "physical_activity","heavy_alcohol_consumption","healthcare","general_health_feeling","mental_health_feeling",
                "physical_health_feeling","education",]
        data = all_entries[cols].copy()
        # encoder = LabelEncoder()
        # data.loc[:,"sex"] = encoder.fit_transform(data.loc[:,"sex"])
        # male = 1, female = 0
        y = data.iloc[:,0] #  - zmienna, którą będziemy chcieli przewidzieć
        x = data.iloc[:,1:15] # zmienne na podstawie, których chcemy przewidzieć
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

    def model(X_train, y_train):
        forest = RandomForestClassifier( n_estimators=10, random_state=0)
        forest.fit(X_train,y_train)
        print("Las: {0}".format(forest.score(X_train,y_train)) )
        
        lreg =LogisticRegression()
        lreg.fit(X_train,y_train)
        print("Regresja logistyczna: {0}".format(lreg.score(X_train,y_train)) )
    
        tree =DecisionTreeClassifier()
        tree.fit(X_train,y_train)
        print("Drzewa decyzyjne: {0}".format(tree.score(X_train,y_train)) )

        target_names=["not sick","sick"]
        y1_predict = forest.predict(X_test)
        print("Random Forest {0}".format(accuracy_score(y_test, y1_predict)))

        y2_predict = lreg.predict(X_test)
        print("Logistic Regresion {0}".format(accuracy_score(y_test, y2_predict)))

        y3_predict = tree.predict(X_test)
        print("Decision Tree {0}".format(accuracy_score(y_test, y3_predict)))

        forest, lreg, tree = model(X_train,y_train)
# uzyskujemy dzięki temu informacje dotyczącą dokładności modelu 
        return forest, lreg, tree
    def hello(self,request):
        return 'Piotrek'

  
    

