from django import forms
from django.contrib.auth.models import User
from dank_app.models import UserProfile
from django.forms import extras
from django.core import validators
import datetime

class UserForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Retype your Password')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                raise forms.ValidationError("The two password fields didn't match.")
        return password2

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password','password2')


class UserProfileForm(forms.ModelForm):
    #date range between this year and upto 120 (oldest a peson has lived is 116)
    current_year = datetime.date.today().year
    dateOfBirth=forms.DateField(widget=forms.extras.SelectDateWidget(years=[year for year in reversed(range(current_year-120,current_year))]),
                                label='Date of Birth')
    class Meta:
        model = UserProfile
        fields = ('dateOfBirth')
