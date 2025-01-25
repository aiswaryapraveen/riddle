from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email']

class CombinedUserForm(UserUpdateForm, PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        UserUpdateForm.__init__(self, *args, instance=user, **kwargs)
        PasswordChangeForm.__init__(self, user, *args, **kwargs)

    def save(self, commit=True):
        # Save user details
        user = super(UserUpdateForm, self).save(commit=False)
        
        # Save the new password if provided
        if self.cleaned_data.get('new_password1'):
            user.set_password(self.cleaned_data['new_password1'])

        if commit:
            user.save()

        return user
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Include email

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
