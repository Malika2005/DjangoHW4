from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gym_group = models.CharField(max_length=80)
    payment_status = models.BooleanField()

    def __str__(self):
        return f'{self.name} - {self.age} - {self.gym_group} - {self.payment_status}'
