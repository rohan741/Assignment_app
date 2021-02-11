
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm # import Registration form to add extra fields
from django import forms
from django.contrib.auth.models import User

# new form defined containing default fields with new added fields
class registerform(UserCreationForm):
	email=forms.EmailField()
	first_name= forms.CharField(max_length=20)
	last_name=forms.CharField(max_length=20)
	DOB= forms.CharField()
	
	class Meta:
		model=User
		fields=['email', 'username', 'first_name', 'last_name', 'DOB', 'password1', 'password2']
		
	def save(self, commit=True):
	    user = super (registerform , self ).save(commit=False)
	    user.first_name = self.cleaned_data ['first_name']
	    user.last_name = self.cleaned_data ['last_name']
	    user.email = self.cleaned_data ['email']
	    user.is_staff = True
	    user.is_superuser=True #it will make user as superuser
		
	    if commit :
		    user.save()
		
	    return user
	
	