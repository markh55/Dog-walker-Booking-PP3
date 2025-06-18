from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator
# from django.contrib.auth.models import User


# Create your models here.
class Walk(models.Model):
    TIME_CHOICES = [
        ('MORNING', 'Morning'),
        ('AFTERNOON', 'Afternoon'),
    ]
    walker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Dog Walker
    date = models.DateField()
    time_of_day = models.CharField(max_length=10, choices=TIME_CHOICES)
    number_of_dogs = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2)])
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['walker', 'date', 'time_of_day'] # No double bookings for the walker at the same time & date

    def __str__(self):
        return f"Walk on {self.date} with {self.number_of_dogs} dog(s)"    
    
class Booking(models.Model):
    SIZE_CHOICES = [ # Dog size options
        ('SMALL', 'Small (0–7 kg)'),
        ('MEDIUM', 'Medium (8–18 kg)'),
        ('LARGE', 'Large (19–45 kg)'),
        ('XL', 'Extra Large (46+ kg)'),
    ]
    walk = models.OneToOneField(Walk, on_delete=models.CASCADE, related_name='bookings') # Each walk can have one booking
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Dog owner

    dog_size = models.CharField(max_length=6, choices=SIZE_CHOICES) # Dog size booked

    created_at = models.DateTimeField(auto_now_add=True) # Booking creation timestamp
    class Meta:
        unique_together = ['walk', 'owner']  # Prevent owner from booking same walk twice

    def __str__(self):
        return f"{self.owner.get_full_name()} booked a {self.dog_size.lower()} dog for {self.walk}" 
    
class Review(models.Model):
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_written')
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating}★ by {self.reviewer}"