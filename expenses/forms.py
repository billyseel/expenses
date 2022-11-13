from django import forms
from . models import Expenses


class ExpenseModelForm(forms.ModelForm):

    class Meta:
        model = Expenses
        # the model above is equal to expenses more or less meaning that we are importing the expenses model
        fields = '__all__'
        # here we want to import all the fields on the models class. if we want to import only a few of them
        # we could use ['put fild inside quotes', 'separete with commas']the above model and fields are necessary

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # <input type='text' class='form-control'>
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
        # here we say the attributes of each model imported .ex name will take a text input and price will take a number input

        labels = {
            'name': 'product name',
            # if we want to display a different name on the webpage, we could use labels.
            # besides this we have to rember to mentions on html file . ex<label>{{ form.name.label }}</label>
            'price': 'value'
        }
