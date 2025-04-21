from django import forms
from .models import JobApplication

class JobForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'
        widgets = {
            'applied_on': forms.DateInput(attrs={'type': 'date'}),
        }
