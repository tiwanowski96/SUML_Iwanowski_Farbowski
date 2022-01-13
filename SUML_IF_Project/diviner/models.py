from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Diabetes(models.Model):
    sick = models.BooleanField(
        null=False,
        default = False
    )
    SEX = [
        (1, 'female'),
        (0, 'male')
    ]
    sex = models.IntegerField(
        null=False,
        choices=SEX,
        default = 1
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
        default=0
    )
    CHOLESTEROL = [
        (1, 'HighCholesterol'),
        (0, 'LowCholesterol')
    ]
    cholesterol = models.IntegerField(
        choices=CHOLESTEROL,
        null=False,
        default=0
    )
    bmi = models.IntegerField(null=False, default=20)
    smoker = models.BooleanField(null=False, default = False)
    stroke = models.BooleanField(null=False, default = False)
    heart_disease_or_attack = models.BooleanField(null=False, default = False)
    physical_activity = models.BooleanField(null=False, default = False)
    heavy_alcohol_consumption = models.BooleanField(null=False, default = False)
    healthcare = models.BooleanField(null=False, default = False)
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
        default=3
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
        default=5
    )

    def __str__(self):
        return self.sick
