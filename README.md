# SUML - Iwanowski Farbowski
## The purpose of the project
Diabetes is among the most prevalent chronic diseases in the world, it's a serious chronic disease in which individuals lose the ability to effectively regulate levels of glucose in the blood, and can lead to reduced quality of life and life expectancy or even predecease.
- What risk factors are most predictive of diabetes risk?
- Can we predict the diabetes risk based on factors?

## Model ML

Three models have been calculated:
* Random Forest
* Logistic Regression
* Decision Tree
By switching to the "Train model" view, the application creates new models each time based on the objects in the Diabetes table. The application is responsible for the selection of the appropriate model, on its basis, prediction is calculated.

## Description of the functionality

The user can enter data in two ways:
* by adding a csv file with data
* by filling out the patient's form
The user can re-train the model at any time by going to the train model view.
The most important functionality of the project is to predict, based on the available data, the likelihood of a patient suffering from diabetes.

## Django
The project is built on the Django framework.

Documentation: https://docs.djangoproject.com/en/4.0/  
Installation guide: https://docs.djangoproject.com/en/4.0/intro/install/

## Requirements
* Python 3.x.y
* Django 4.0.1
* psycopg2>=2.8
* pandas
* numpy
* matplotlib
* seaborn
* sklearn

## Prepare development environment (1st option - Docker)
1. Check if you have docker installed, if not you need to install it.

Installation: https://docs.docker.com/get-docker/
Docker documetation: https://docs.docker.com/

2. Move to the main directory `/SUML_Iwanowski_Farbowski` and run below command:
```
$ docker-compose up
```
3. Application is available under http://localhost:8000/diviner/ URL.

## Prepare development environment (2nd option - virtual environment)
1. Check if you have Python installed, if not you need to install it.  
```
$ python3 -V
Python 3.8.10
```
2. In the main directory `/SUML_Iwanowski_Farbowski` create virtual environment.  
```
$ python3 -m venv {name}
```
3. Activate your virtual environment.  
```
$ source {name}/bin/activate
```
4. Check your pip.  
```
$ pip3 -V
pip 20.0.2 from /home/tiwan/PJATK/SUML/SUML_Iwanowski_Farbowski/venv/lib/python3.8/site-packages/pip (python 3.8)
```
5. Install requirements.
```
$ pip3 install -r requirements.txt
```

### How to launch the application?  
1. Clone this repository.
2. Enter the `/SUML_Iwanowski_Farbowski/SUML_IF_Project` directory.
3. Start the server.  
```
$ python manage.py runserver
```

### Data

The data used by us in the project come from the kaddle data set:

https://www.kaggle.com/alexteboul/diabetes-health-indicators-dataset

To quote the data owner:

"The Behavioral Risk Factor Surveillance System (BRFSS) is a health-related telephone survey that is collected annually by the CDC. Each year, the survey collects responses from over 400,000 Americans on health-related risk behaviors, chronic health conditions, and the use of preventative services. It has been conducted every year since 1984. For this project, a csv of the dataset available on Kaggle for the year 2015 was used. This original dataset contains responses from 441,455 individuals and has 330 features. These features are either questions directly asked of participants, or calculated variables based on individual participant responses."

The csv file is located in the root directory of the project (`diabetes.csv`)

#### Grupa 3
Piotr Farbowski  
Tomasz Iwanowski

Trello: https://trello.com/b/B58ciuVO/grupa-3
