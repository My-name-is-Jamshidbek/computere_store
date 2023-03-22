from django import forms
from .models import Installment

class InstallmentForm(forms.ModelForm):
    class Meta:
        model = Installment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'months': forms.NumberInput(attrs={'class': 'form-control'}),
            'percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'minimum_money': forms.NumberInput(attrs={'class': 'form-control'}),
            'maximum_money': forms.NumberInput(attrs={'class': 'form-control'}),
        }
