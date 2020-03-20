from django.db import models
from django.contrib.auth.models import (
		AbstractBaseUser)

# Create your models here.
'''class User(AbstractBaseUser):
	email = models.EmailField(max_length=255, unique=True)
	full_name = models.CharField(max_length=255, blank=True, null=True)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) # Staff
	admin = models.BooleanField(default=False) # Operator

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = []

	def __str__(self):
		return

	def get_full_name(self):
		return

	def get_short_name(self):
		return

	@property
	def is_admin(self):
		return self.staff

	def is_active(self):
		return self.active

class Profile(models.Model):
	user = models.OneToOneField(User)'''
