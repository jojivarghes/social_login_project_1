from django import forms


class SearchForm(forms.Form):
    phone_number = forms.CharField(label='Phone number', max_length=12)
