from django.db import models
from django.utils import timezone

class Reminder(models.Model):
    DELIVERY_METHODS = (
        ('SMS', 'SMS'),
        ('EMAIL', 'Email'),
    )
    
    delivery_date = models.DateField(null=False, blank=False)
    delivery_time = models.TimeField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_METHODS)
    created_at = models.DateTimeField(auto_now_add=True) #It will automatically save date and time when the object is created
    
    def __str__(self):
        return f"{self.message} on {self.delivery_date} at {self.delivery_time} via {self.delivery_method}"