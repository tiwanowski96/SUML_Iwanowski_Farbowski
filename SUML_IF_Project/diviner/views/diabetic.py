"""System module."""
from django.shortcuts import render
from django.views import View
from diviner.models import Diabetes


class DiabetesView(View):
    '''View of Diabetes details'''
    def get(self, request, id):
        '''Get individual object from Diabetes model'''
        diabetic = Diabetes.objects.get(id=id)
        ctx = {'diabetic': diabetic}
        return render(request, 'diviner/diabetic.html', ctx)
