from django import forms
from diviner.models import Diabetes


class DiabetesAddForm(forms.ModelForm):
    class Meta:
        model = Diabetes
        fields = [
            'sick',
            'sex',
            'age',
            'high_blood_preasure',
            'cholesterol',
            'bmi',
            'smoker',
            'stroke',
            'heart_disease_or_attack',
            'physical_activity',
            'heavy_alcohol_consumption',
            'healthcare',
            'general_health_feeling',
            'mental_health_feeling',
            'physical_health_feeling',
            'education'
        ]
    

class DiabeticPredictionForm(forms.ModelForm):
    class Meta:
        model = Diabetes
        fields = [
            'sex',
            'age',
            'high_blood_preasure',
            'cholesterol',
            'bmi',
            'smoker',
            'stroke',
            'heart_disease_or_attack',
            'physical_activity',
            'heavy_alcohol_consumption',
            'healthcare',
            'general_health_feeling',
            'mental_health_feeling',
            'physical_health_feeling',
            'education'
        ]