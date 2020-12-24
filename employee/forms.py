from django import forms
from django.contrib.auth.models import User
from .models import Profile

class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', help_text='First Name')
    last_name = forms.CharField(label='First Name', help_text='Last Name')
    username = forms.CharField(label='First Name', help_text='Username')

    class Meta:
        model = User

        fields = [ 'first_name', 'last_name', 'email', 'username', 'password' ]
        label = { 'password': 'Password' }

    def save(self):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.set_password(password)
        u.save()

class EmployeeProfileForm(forms.ModelForm):
    designation = forms.CharField(label='',
        widget=forms.TextInput(attrs = { "placeholder": "Your salary", "class": "form-control" }))
    salary = forms.CharField(label='Salary',
        widget=forms.TextInput(attrs = { "placeholder": "Your salary", "class": "form-control" }))
    sort_bio = forms.CharField(
                label='About Me',
                widget=forms.Textarea(
                    attrs={
                        "class": "form-control",
                        "rows": 5,
                        "cols": 10
                    }
                )
            )

    class Meta:
        model = Profile
        fields = [
            'designation',
            'salary',
            'sort_bio'
        ]
