from django import forms
from logreg.models import User


class UserProfileFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ["profile_pic"]