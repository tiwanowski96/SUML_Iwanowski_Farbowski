from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Diabetes(models.Model):
    sick = models.BooleanField(null=True)
    SEX = [
        (1, 'female'),
        (0, 'male')
    ]
    sex = models.BooleanField(
        null=True,
        choices=SEX
    )
    age = models.IntegerField(null=True)
    HIGH_BP = [
        (1, 'HighBloodPreasure'),
        (0, 'LowBloodPreasure')
    ]
    high_blood_preasure = models.IntegerField(
        choices=HIGH_BP,
        null=True
    )
    CHOLESTEROL = [
        (1, 'HighCholesterol'),
        (0, 'LowCholesterol')
    ]
    cholesterol = models.IntegerField(
        choices=CHOLESTEROL,
        null=True
    )
    bmi = models.IntegerField(null=True)
    smoker = models.BooleanField(null=True)
    stroke = models.BooleanField(null=True)
    heart_disease_or_attack = models.BooleanField(null=True)
    physical_activity = models.BooleanField(null=True)
    heavy_alcohol_consumption = models.BooleanField(null=True)
    healthcare = models.BooleanField(null=True)
    GENERAL_HEALTH_FEELING = [
        (1, 'excellent'),
        (2, 'very good'),
        (3, 'good'),
        (4, 'fair'),
        (5, 'poor')
    ]
    general_health_feeling = models.IntegerField(
        choices=GENERAL_HEALTH_FEELING,
        null=True
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
        null=True
    )

    def __str__(self):
        return self.sick
