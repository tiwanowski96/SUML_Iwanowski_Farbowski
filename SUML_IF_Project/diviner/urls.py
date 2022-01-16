from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_form/', views.upload_form, name='upload_form'),
    path('add_diabetes/', views.DiabetesAddView.as_view(), name='add_diabetes'),
    path('diabetic/<int:id>/', views.DiabetesView.as_view(), name='diabetic'),
    path('diabetic_prediction/', views.DiabeticPredictionView.as_view(), name='diabetic_prediction'),
]