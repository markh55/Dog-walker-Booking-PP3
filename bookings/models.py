from django.db import models
from django.conf import settings


# Create your models here.
class Walk(models.Model):
    TIME_CHOICES = [
        ('MORNING', 'Morning'),
        ('AFTERNOON', 'Afternoon'),
    ]
    walker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Dog Walker
    date = models.DateField()
    time_of_day = models.CharField(max_length=10, choices=TIME_CHOICES)
    number_of_dogs = models.PositiveSmallIntegerField()
    dog_owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['walker', 'date', 'time_of_day'] # No double bookings for the walker at the same time & date

    def __str__(self):
        return f"Walk on {self.date} with {self.number_of_dogs} dog(s)"