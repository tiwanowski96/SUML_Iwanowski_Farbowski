import base64
import pickle
import os
import pandas as pd
import seaborn as sns

from django.shortcuts import render
from django.views.generic import View
from io import BytesIO

class HomeView(View):
    '''Home page view'''

    def get(self, request):        
        '''Home page data'''
        plot = self.plot()
        plot2 = self.plot2()
        return render(request, 'diviner/home.html')


    def plot(request):
        '''render plot'''
        try:
            os.remove("SUML_IF_Project/diviner/static/diviner/plot.png")
        except IOError:
            pass   
        try:
            all_entries = pd.read_csv('diabetes.csv')
            all_entries.columns
            cols = ["sick","sex","age","high_blood_preasure","cholesterol","bmi","smoker","stroke","heart_disease_or_attack",
                    "physical_activity","heavy_alcohol_consumption","healthcare","general_health_feeling","mental_health_feeling",
                    "physical_health_feeling","education"]
            data = all_entries[cols].copy()
            print('data: %s' % data)
            data.isnull().any()
            sns.set_style('whitegrid')
            sick_plot = sns.countplot(x='sick', data=data)
            fig = sick_plot.get_figure()
            plot_png = fig.savefig("SUML_IF_Project/diviner/static/diviner/plot.png") 
            return plot_png
        except IOError:
            return


    def plot2(request):
        '''render variable dependency'''
        try:
            os.remove("SUML_IF_Project/diviner/static/diviner/variable_dependency.png")
        except IOError:
            pass   
        try:
            all_entries1 = pd.read_csv('diabetes.csv')
            all_entries1.columns     
            all_entries1 = all_entries1[["sick","sex","age","high_blood_preasure","cholesterol","bmi","smoker","stroke","heart_disease_or_attack",
                    "physical_activity","heavy_alcohol_consumption","healthcare","general_health_feeling","mental_health_feeling",
                    "physical_health_feeling","education"]].dropna()
            y = all_entries1.pop('sick')
            imported_model = pickle.load(open("forest_model.sv", 'rb'))
            imported_model.fit(all_entries1 ,y)   
            variable_dependency = (pd.Series(imported_model.feature_importances_, index=all_entries1.columns)
            .nlargest(16).plot(kind='barh')) 
            fig1 = variable_dependency.get_figure()
            variable_dependency_png = fig1.savefig("SUML_IF_Project/diviner/static/diviner/variable_dependency.png")
            return variable_dependency_png
        except IOError:
            return        
    


