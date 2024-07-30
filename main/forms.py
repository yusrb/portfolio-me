from django import forms
from .models import ContactProfile

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Full name..',
            'class': 'block w-full mt-1 border border-gray-300 rounded-md shadow-sm focus:ring-teal-500 focus:border-teal-500'
        })
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Email..',
            'class': 'block w-full mt-1 border border-gray-300 rounded-md shadow-sm focus:ring-teal-500 focus:border-teal-500'
        })
    )
    message = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': '*Message..',
            'class': 'block w-full mt-1 border border-gray-300 rounded-md shadow-sm focus:ring-teal-500 focus:border-teal-500',
            'rows': 6,
        })
    )

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message',)
