from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_form/', views.upload_form, name='upload_form')
]