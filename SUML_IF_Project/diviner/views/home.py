import base64
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from django.shortcuts import render
from django.views.generic import View
from io import BytesIO

class HomeView(View):

    def get(self, request):        
        
        plot = self.plot(self)
        return render(request, 'diviner/home.html')

    def plot(self, request):

        all_entries = pd.read_csv('diabetes.csv')
        all_entries.columns
        cols = ["sick","sex","age","high_blood_preasure","cholesterol","bmi","smoker","stroke","heart_disease_or_attack",
                "physical_activity","heavy_alcohol_consumption","healthcare","general_health_feeling","mental_health_feeling",
                "physical_health_feeling","education"]
        data = all_entries[cols].copy()
        print('data: %s' % data)
        data.isnull().any()
        sns.set_style('whitegrid')
        plot = sns.countplot(x='sick', data=data)
        fig = plot.get_figure()
        plot_png = fig.savefig("SUML_IF_Project/diviner/static/diviner/plot.png") 

        return plot_png
