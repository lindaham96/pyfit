from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.postgres.forms import SimpleArrayField

from .constants import DAYS_OF_WEEK
from .models import Routine, Exercise, ExerciseHistory


def clean_cleaned_data(data):
    """For removing empty fields from cleaned data"""
    return {k: v for k, v in data.items() if v is not ''}


class CustomModelForm(forms.ModelForm):
    def clean(self):
        data = super(CustomModelForm, self).clean()
        return clean_cleaned_data(data)


class RegistrationForm(forms.Form):
    username = forms.EmailField(max_length=250)
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'name': 'password',
                'id': 'password',
                'class': 'password',
                'placeholder': 'Password'
            }
        ),
        label='Password',
        error_messages={
            'required': 'Please enter your password.'
        }
    )
    password_confirm = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'name': 'password_confirm',
                'id': 'password_confirm',
                'class': 'password',
                'placeholder': 'Confirm Password'
            }
        ),
        label='Confirm Password',
        error_messages={
            'required': 'Please re-enter your password.'
        }
    )

    def clean(self):
        data = super(RegistrationForm, self).clean()
        if data['password'] != data['password_confirm']:
            self.add_error('password', 'Passwords do not match.')
            return
        data['email'] = data['username']

    def save(self):
        self.cleaned_data.pop('password_confirm')
        user = User.objects.create_user(**self.cleaned_data)
        return {
            'username': user.username,
            'password': self.cleaned_data.get('password'),
        }


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=250)
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'name': 'password',
                'id': 'password',
                'class': 'password',
                'placeholder': 'Password'
            }
        ),
        label='Password',
        error_messages={
            'required': 'Please enter your password.'
        }
    )

    def confirm_login_allowed(self, user):
        pass


class RoutineForm(CustomModelForm):
    day = forms.ChoiceField(choices=DAYS_OF_WEEK, required=False)
    name = forms.CharField(max_length=250, required=False)

    class Meta:
        model = Routine
        fields = ['day', 'name']


class ExerciseForm(CustomModelForm):
    sets = SimpleArrayField(forms.IntegerField(), required=False)
    rest_duration = forms.IntegerField(initial=60, required=False)
    name = forms.CharField(max_length=250, required=False)
    exercise_type = forms.CharField(max_length=250, required=False)

    class Meta:
        model = Exercise
        fields = ['sets', 'rest_duration', 'name', 'exercise_type']


class ExerciseHistoryForm(CustomModelForm):
    sets = SimpleArrayField(forms.IntegerField(), required=False)
    weights_per_set = SimpleArrayField(forms.IntegerField(), required=False)

    class Meta:
        model = ExerciseHistory
        fields = ['sets', 'weights_per_set']
