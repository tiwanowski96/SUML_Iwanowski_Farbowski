import csv, io
from django.http import HttpResponse
from django.shortcuts import render
from ..models import Diabetes


def upload_form(request):
    template = 'diviner/upload_form.html'
    data = Diabetes.objects.all()

    prompt = {
        'csv': 'Diabetes CSV',
        'diabetes': data    
    }

    if request.method == "GET":
        return render(request, template, prompt)

    if request.method == "POST":
        csv_file = request.FILES['file']

        # TODO validation
        # if not csv_file.name.endswith('.csv'):
        #     return HttpResponse('THIS IS NOT A CSV FILE')
        # else:
        data_set = csv_file.read().decode('UTF-8')

        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            diabetic = Diabetes(
                sick=column[0],
                sex=column[1],
                age=column[2],
                high_blood_preasure=column[3],
                cholesterol=column[4],
                bmi=column[5],
                smoker=column[6],
                stroke=column[7],
                heart_disease_or_attack=column[8],
                physical_activity=column[9],
                heavy_alcohol_consumption=column[10],
                healthcare=column[11],
                general_health_feeling=column[12],
                mental_health_feeling=column[13],
                physical_health_feeling=column[14],
                education=column[15]
            )
            diabetic.save()
        return render(request, template, prompt)