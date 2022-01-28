"""System module."""
import pickle
import pandas as pd

from django.shortcuts import redirect, render
from django.views.generic import View
from sklearn.model_selection import train_test_split
from ..forms import DiabeticPredictionForm
from ..models import Diabetes


class DiabeticPredictionView(View):
    '''View for predicting a patient's illness'''

    def get(self, request):
        '''Render diabetic_prediction template with context'''
        form = DiabeticPredictionForm()
        ctx = {'form': form}
        return render(request, 'diviner/diabetic_prediction.html', ctx)


    def post(self, request):
        '''Predicting the patient's disease based on the data provided in the form'''
        form = DiabeticPredictionForm(data=request.POST)
        ctx = {'form': form}

        if form.is_valid():
            # Validate boolean fields
            # “on” value must be either True or False.
            smoker=self.validate_boolean_field(request.POST.get('smoker'))
            stroke=self.validate_boolean_field(request.POST.get('stroke'))
            heart_disease_or_attack=self.validate_boolean_field(
                request.POST.get('heart_disease_or_attack')
            )
            physical_activity=self.validate_boolean_field(
                request.POST.get('physical_activity')
            )
            heavy_alcohol_consumption=self.validate_boolean_field(
                request.POST.get('heavy_alcohol_consumption')
            )
            healthcare=self.validate_boolean_field(request.POST.get('healthcare'))

            data = [
                [
                    request.POST.get('sex'),
                    request.POST.get('age'),
                    request.POST.get('high_blood_preasure'),
                    request.POST.get('cholesterol'),
                    request.POST.get('bmi'),
                    smoker,
                    stroke,
                    heart_disease_or_attack,
                    physical_activity,
                    heavy_alcohol_consumption,
                    healthcare,
                    request.POST.get('general_health_feeling'),
                    request.POST.get('mental_health_feeling'),
                    request.POST.get('physical_health_feeling'),
                    request.POST.get('education')
                ]
            ]

            # Prediction
            x, y, X_test, y_test = self.prepare_test_data(self)

            imported_model = pickle.load(open("model.sv", 'rb'))
            imported_model.fit(x.values ,y)
            prediction = imported_model.predict(data)
            print(f'prediction {prediction[0]}')
            prediction_proba = imported_model.predict_proba(data)
            print(f'prediction_proba {prediction_proba}')

            # Create new object of Diabetes model
            diabetic = Diabetes(
                sick = prediction[0],
                sex=request.POST.get('sex'),
                age=request.POST.get('age'),
                high_blood_preasure=request.POST.get('high_blood_preasure'),
                cholesterol=request.POST.get('cholesterol'),
                bmi=request.POST.get('bmi'),
                smoker=smoker,
                stroke=stroke,
                heart_disease_or_attack=heart_disease_or_attack,
                physical_activity=physical_activity,
                heavy_alcohol_consumption=heavy_alcohol_consumption,
                healthcare=healthcare,
                general_health_feeling=request.POST.get('general_health_feeling'),
                mental_health_feeling=request.POST.get('mental_health_feeling'),
                physical_health_feeling=request.POST.get('physical_health_feeling'),
                education=request.POST.get('education'),
                prediction_proba=prediction_proba
            )

            diabetic.save()
            return redirect(f'/diviner/diabetic/{diabetic.id}')

        else:
            return render(request, 'diviner/diabetic_prediction.html', ctx)


    def validate_boolean_field(self, field):
        '''Validate form's boolean field'''

        if field == 'on':
            field = 1
        else:
            field = 0

        return field


    def prepare_test_data(self, request):
        '''Preparation of test data based on the csv file'''
        try:
            f = open("diabetes.csv")
        except IOError:
            return render(request, 'diviner/model_empty.html')

        all_entries = pd.read_csv('diabetes.csv')
        all_entries.columns
        cols = [
            "sick",
            "sex",
            "age",
            "high_blood_preasure",
            "cholesterol",
            "bmi",
            "smoker",
            "stroke",
            "heart_disease_or_attack",
            "physical_activity",
            "heavy_alcohol_consumption",
            "healthcare",
            "general_health_feeling",
            "mental_health_feeling",
            "physical_health_feeling",
            "education"
        ]
        data = all_entries[cols].copy()
        print(f'data: {data}')
        data.isnull().any()
        y = data.iloc[:,0] #  - zmienna, którą będziemy chcieli przewidzieć
        x = data.iloc[:,1:16] # zmienne na podstawie, których chcemy przewidzieć
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
        return x, y, X_test, y_test
