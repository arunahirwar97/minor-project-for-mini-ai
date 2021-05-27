from django import forms 
from .models import *
  
class ocr_forms(forms.ModelForm): 
  
    class Meta: 
        model = ocr_model 
        fields = ['image'] 