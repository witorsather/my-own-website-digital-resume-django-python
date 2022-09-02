from django import forms
# ME - email, message that's what we're tryng to capture here
# file models.py with class ContactProfile(models.Model):
# is the model that we made in the 
from .models import ContactProfile

# we need create variables one for each field that we want in the form
class ContactForm(forms.ModelForm):
    # is what will be rendered in the html on the front end
    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Full name..',
            'class': 'form-control'
        }))
    email = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Email..',
            'class': 'form-control'
        }))
    message = forms.CharField(max_length=1000, required=True,
        widget=forms.Textarea(attrs={
            # it's not a text input it's a text area
            'placeholder': '*Message..',
            'class': 'form-control',
            # rows in text area
            'rows': 6,
        }))

    # this represents is contact profile and fields that we want to render is name, email, message
    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message',)
    