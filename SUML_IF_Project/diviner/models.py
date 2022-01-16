from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Diabetes(models.Model):
    sick = models.BooleanField(
        null=False,
        default=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1)
        ]
    )
    SEX = [
        (1, 'female'),
        (0, 'male')
    ]
    sex = models.IntegerField(
        null=False,
        choices=SEX,
        default = 1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1)
        ]
    )
    age = models.IntegerField(
        null=False,
        default=50
    )
    HIGH_BP = [
        (1, 'HighBloodPreasure'),
        (0, 'LowBloodPreasure')
    ]
    high_blood_preasure = models.IntegerField(
        choices=HIGH_BP,
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1)
        ]
    )
    CHOLESTEROL = [
        (1, 'HighCholesterol'),
        (0, 'LowCholesterol')
    ]
    cholesterol = models.IntegerField(
        choices=CHOLESTEROL,
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1)
        ]
    )
    # BMI = [
    #     (range(0,18),'underweight'),
    #     (range(19,25),'healthy weight'),
    #     (range(26,30),'overweight'),
    #     (range(31,40),'obese')
    # ]
    bmi = models.IntegerField(
        # choices=BMI,
        null=False,
        default=20,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(40)
        ]
    )
    smoker = models.BooleanField(default = False)
    stroke = models.BooleanField(default = False)
    heart_disease_or_attack = models.BooleanField(default = False)
    physical_activity = models.BooleanField(default = False)
    heavy_alcohol_consumption = models.BooleanField(default = False)
    healthcare = models.BooleanField(default = False)
    GENERAL_HEALTH_FEELING = [
        (1, 'excellent'),
        (2, 'very good'),
        (3, 'good'),
        (4, 'fair'),
        (5, 'poor')
    ]
    general_health_feeling = models.IntegerField(
        choices=GENERAL_HEALTH_FEELING,
        null=False,
        default=3,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    mental_health_feeling = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(31)
        ]
    )
    physical_health_feeling = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(31)
        ]
    )
    EDUCATION = [
        (1, 'never attended'),
        (2, 'kindergarden'),
        (3, 'primary school'),
        (4, 'junior high school'),
        (5, 'high school'),
        (6, 'college')
    ]
    education = models.IntegerField(
        choices=EDUCATION,
        null=False,
        default=5,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)
        ]
    )

    def __str__(self):
        return self.sick
