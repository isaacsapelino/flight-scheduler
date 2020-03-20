from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Flights

class FlightsForm(ModelForm):
	class Meta:
		model = Flights
		fields = ['name', 'desc', 'dest', 'imageFile', 'price']

class AddFlightsForm(forms.Form):
	flights_name = forms.CharField(label='Name of travel:', max_length=100, widget=forms.TextInput(attrs={
			'class' : 'form-control'
		}))
	flights_desc = forms.CharField(label='Description', widget=forms.Textarea(attrs={
		'placeholder' : 'Write your own purpose for the travel. :)'
		}))
	flights_start = forms.DateField(label='Start of travel', widget=forms.DateInput(attrs={
			'data-provide' : 'datepicker',
			'class' : 'form-control input-group date',
			'data' : '#datetimepicker1'
		}))
	flights_end = forms.DateField(label='End of travel', widget=forms.DateInput(attrs={
			'data-provide' : 'datepicker',
			'class' : 'form-control input-group date',
			'data' : '#datetimepicker1'
		}))

	'''def __init__(self, name, *args, **kwargs):
		super(AddFlightsForm, self).__init__(*args, **kwargs)
		self.fields['flights_name'].queryset = Booker.objects.filter(user=user)'''

	'''def __init__(self, name, *args, **kwargs):
		super(AddFlightsForm, self).__init__(*args, **kwargs)
		self.fields['flights_name'].queryset = Booker.objects.filter(user=user)'''