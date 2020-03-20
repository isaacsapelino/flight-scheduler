from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.

class Flights(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    dest = models.CharField(max_length=100, blank=True)
    imageFile = models.ImageField(upload_to='places/', null=True, blank=True)
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=7, default=1000)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return reverse("add_flight_plan",kwargs={"id":self.id})

class Booker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Booker.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=User)

# Handles Users to Plan their Flights
class Planner(models.Model):
    flights = models.OneToOneField(Flights, on_delete=models.SET_NULL, null=True)
    booker = models.ForeignKey(Booker, on_delete=models.SET_NULL, null=True)
    is_planned = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.flights.name

# Planned Flights
class PlannedFlights(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Flights, null=True)
    desc = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    planned = models.BooleanField(default=False, verbose_name='Planned')

    def __str__(self):
        return self.user.username
