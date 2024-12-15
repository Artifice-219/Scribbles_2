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


# this form will be used to collect form data
class login_form(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'mt-2 block w-full px-4 py-3 border border-gray-300 rounded-3xl shadow-sm placeholder-gray-400 text-black focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-base'
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'mt-2 block w-full px-4 py-3 border border-gray-300 rounded-3xl shadow-sm placeholder-gray-400 text-black focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-base'
        })
    )
