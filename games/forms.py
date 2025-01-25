from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email']

class CombinedUserForm(UserUpdateForm, PasswordChangeForm):
    """
    Combines user details update and password change in a single form.
    """
    def __init__(self, user, *args, **kwargs):
        UserUpdateForm.__init__(self, *args, instance=user, **kwargs)
        PasswordChangeForm.__init__(self, user, *args, **kwargs)
