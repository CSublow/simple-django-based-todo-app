from django import forms
from .models import Item

# This works by creating a class that inherits from forms.ModelForm
class ItemForm(forms.ModelForm):
    # In order to generate the form you need to create an inner class called Meta. This allows you to to customise the form
    class Meta:
        model = Item # The form will be based off the Item model
        fields = ('name', 'done')
        