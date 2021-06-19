from django import forms
from .models import Transaction, People

class TransactonForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'slug', 'amount', 'people']


class PeopleForm(forms.ModelForm):

    class Meta:
        model = People
        fields = ['fullname', 'username']