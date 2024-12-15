from django import forms
from .models import User, Letter


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password using the set_password method
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



# JESS STRUCTURE.
# from django import forms


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['title', 'recipient', 'content']
