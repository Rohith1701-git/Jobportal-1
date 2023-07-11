from django.forms import ModelForm, Textarea
from django import forms
from .models import *
# from django import forms

class ApplyForm(ModelForm):
    class Meta:
        model=Candidates
        fields=["candidate_user", "resume", "company"]

class UserWithRoleForm(ModelForm):
    class Meta:
        model=UserWithRole
        fields="__all__"
        exclude = ['create_by']
        widgets = { 
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'companyname':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.TextInput(attrs={'class':'form-control'}),
            'password2':forms.TextInput(attrs={'class':'form-control'}),
            'role':forms.Select(attrs={'class':'form-control'}),
            'dob': forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'},format='%Y-%m-%d')
        }

class Companyform(ModelForm):
    
    class Meta:
        model=Company
        fields="__all__" 
        exclude = ['user']