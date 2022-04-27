from django import forms
from .models import UserProfile
from django_countries.fields import CountryField

class ContactForm(forms.ModelForm):
    """ User Profile Information Form """
    class Meta:
        model = UserProfile
        fields = (
            'default_phone_number',
            'default_street_adress',
            'default_city',
            'default_postal_code',
            'default_co',
            'default_country'
        )
        labels = {
            'default_phone_number': 'Phone Number',
            'default_street_adress': 'Street Address',
            'default_city': 'City/Town',
            'default_postal_code': 'Zip/Postal Code',
            'default_co': 'C/O',
            'default_country': 'Country'
        }

        # widgets = {
        #     'default_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'default_street_adress': forms.TextInput(attrs={'class': 'form-control'}),
        #     'default_city': forms.TextInput(attrs={'class': 'form-control'}),
        #     'default_postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        #     'default_co': forms.TextInput(attrs={'class': 'form-control'}),
        #     'default_country': CountryField(attrs={'class': 'form-control'})
        #     }