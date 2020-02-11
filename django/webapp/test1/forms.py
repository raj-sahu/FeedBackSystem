from django.contrib.auth.models import User
from test1.models import UserProfileInfo,Rating
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

class Ratings(forms.ModelForm):
    choices=[(1,"1"),(2,'2'),(3,'3'),(4,'4'),(5,'5')]
    rate=forms.IntegerField(label="", widget=forms.RadioSelect(choices=choices))
    class Meta():
        model=Rating
        fields = ('question','feedback',)

        widgets = {

            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 10}),
        }
