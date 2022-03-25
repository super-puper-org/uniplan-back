from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    login = models.CharField(max_length=50)
    password = models.CharField()


class Meeting(models.Model):
    location = models.CharField()
    start_time = models.DateTimeField()
    interval = models.DateTimeField()
    color = models.CharField()

    
class Day(models.Model):
    DAY_OF_WEEK = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Th', 'Thursday'),
        ('Fr', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    user_id = models.BigIntegerField()
    meetings = ArrayField(
        ArrayField(Meeting)
    )
