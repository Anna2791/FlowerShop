from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Flower(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='flowers/')
    description = models.TextField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    status_choices = [
        ('pending', 'Принят к работе'),
        ('in_progress', 'Находится в работе'),
        ('delivering', 'В доставке'),
        ('completed', 'Выполнен')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    delivery_address = models.CharField(max_length=255)
    delivery_time = models.DateTimeField(default=now)
    comment = models.TextField(blank=True)