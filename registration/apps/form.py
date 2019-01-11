from django import forms
from django.forms import ModelForm
from .models import*

class studentform(ModelForm):
	class Meta:
		model = newuser
		fields = '__all__'

# class adminform(object):
# 	class Meta:
# 		model = admin_new
# 		fields = '__all__'
