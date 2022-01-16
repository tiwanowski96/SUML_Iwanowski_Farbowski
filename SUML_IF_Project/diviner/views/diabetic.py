from django.shortcuts import render
from django.views import View
from diviner.models import Diabetes


class DiabetesView(View):
    def get(self, request, id):
        diabetic = Diabetes.objects.get(id=id)
        ctx = {'diabetic': diabetic}
        return render(request, 'diviner/diabetic.html', ctx)