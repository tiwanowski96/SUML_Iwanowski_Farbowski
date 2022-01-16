from django.views.generic import CreateView
from django.urls import reverse_lazy
from ..models import Diabetes


class DiabetesAddView(CreateView):
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
    def get_success_url(self):
        return reverse_lazy('diabetic', kwargs={'id': self.object.id})