from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['record_date', 'amount', 'name', 'address']
        widgets = {
            'record_date': forms.DateInput(attrs={'type': 'date'}),
        }
