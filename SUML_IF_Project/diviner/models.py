from django.db import models

class Diabetes(models.Model):
    sick = models.BooleanField(null=True)
    HIGH_BP = [
        (1, 'HighBloodPreasure'),
        (0, 'LowBloodPreasure')
    ]
    high_blood_preasure = models.CharField(
        choices=HIGH_BP,
        null=True,
        max_length=1
    )
    CHOLESTEROL = [
        (1, 'HighCholesterol'),
        (0, 'LowCholesterol')
    ]
    cholesterol = models.CharField(
        choices=CHOLESTEROL,
        null=True,
        max_length=1
    )

    def __str__(self):
        return self.sick
