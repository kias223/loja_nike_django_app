from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class user_creation_from_with_email(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('este email já esta cadastrado')
        return email
