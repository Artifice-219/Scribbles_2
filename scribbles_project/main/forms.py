from django import forms
from .models import User

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Password and Confirm Password do not match")
        return cleaned_data

# JESS STRUCTURE.
# from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['title', 'recipient', 'content']
