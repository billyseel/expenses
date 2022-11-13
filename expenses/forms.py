from django import forms
from . models import Expenses


class ExpenseModelForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'product name',
            'price': 'value'
        }
