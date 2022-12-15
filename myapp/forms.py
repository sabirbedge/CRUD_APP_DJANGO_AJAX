from django import forms
from .models import User
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['nm','mob','city']
        widgets={
            'nm':forms.TextInput(attrs={'class':'form-control','id':'idnm','placeholder':'Name '}),
            'mob':forms.NumberInput(attrs={'class':'form-control','id':'idmob','placeholder':'Mobile'}),
            'city':forms.TextInput(attrs={'class':'form-control','id':'idcity','placeholder':'City'})
        }