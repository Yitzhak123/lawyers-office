
from django import forms
from .models import Lawyer


class LawyerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Lawyer
        fields = ('username', 'email', 'password',)