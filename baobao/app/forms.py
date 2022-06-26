"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import love_bao

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class HomeForm(forms.ModelForm):
    class Meta:
        model = love_bao
        fields=[
            'url_def',
            'banner_pic',
            'left_bao_pic',
            'left_bao_ig',
            'left_bao_des' ,
            'right_bao_pic',
            'right_bao_ig',
            'rights_bao_des' ,
            'bao_together_date',
            'bao_bao_talk',
            'bao_big_thing_date1' ,
            'bao_big_thing_des1',
            'bao_big_thing_date2',
            'bao_big_thing_des2',
            'bao_big_thing_date3',
            'bao_big_thing_des3',
            'bao_big_thing_date4',
            'bao_big_thing_des4',
            'bao_six_pic1' ,
            'bao_six_pic2' ,
            'bao_six_pic3' ,
            'bao_six_pic4' ,
            'bao_six_pic5' ,
            'bao_six_pic6' ]
        widgets = {
            #'user' : forms.
            'url_def' : forms.TextInput(attrs={'class': 'form-control'}),
            'banner_pic' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'left_bao_pic' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'left_bao_ig' : forms.TextInput(attrs={'class': 'form-control'}),
            'left_bao_des' : forms.Textarea(attrs={'class': 'form-control'}),
            'right_bao_pic' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'right_bao_ig': forms.TextInput(attrs={'class': 'form-control'}),
            'rights_bao_des' : forms.Textarea(attrs={'class': 'form-control'}),
            'bao_together_date' : forms.DateInput(attrs={'type':'date'}),
            'bao_bao_talk' : forms.Textarea(attrs={'class': 'form-control'}),
            'bao_big_thing_date1' : forms.DateInput(attrs={'type':'date'}),
            'bao_big_thing_des1' : forms.TextInput(attrs={'class': 'form-control'}),
            'bao_big_thing_date2' : forms.DateInput(attrs={'type':'date'}),
            'bao_big_thing_des2' : forms.TextInput(attrs={'class': 'form-control'}),
            'bao_big_thing_date3' : forms.DateInput(attrs={'type':'date'}),
            'bao_big_thing_des3' : forms.TextInput(attrs={'class': 'form-control'}),
            'bao_big_thing_date4' : forms.DateInput(attrs={'type':'date'}),
            'bao_big_thing_des4' : forms.TextInput(attrs={'class': 'form-control'}),
            'bao_six_pic1' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'bao_six_pic2' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'bao_six_pic3' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'bao_six_pic4' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'bao_six_pic5' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'bao_six_pic6' : forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'url_def' : '自訂寶寶的專屬網址',
            'banner_pic' : '寶寶的甜蜜大圖',
            'left_bao_pic' : '左邊的寶大頭',
            'left_bao_ig' : '左邊的寶ig',
            'left_bao_des' :'左邊的寶介紹',
            'right_bao_pic' : '右邊的寶大頭',
            'right_bao_ig':'右邊的寶ig',
            'rights_bao_des':'右邊的寶介紹' ,
            'bao_together_date':'成為彼此的寶日',
            'bao_bao_talk' : '寶寶的相愛名言',
            'bao_big_thing_date1' :'寶寶大事記1 - 日期',
            'bao_big_thing_des1': '寶寶大事記1 - 描述',
            'bao_big_thing_date2':'寶寶大事記2 - 日期',
            'bao_big_thing_des2': '寶寶大事記2 - 描述',
            'bao_big_thing_date3':'寶寶大事記3 - 日期',
            'bao_big_thing_des3': '寶寶大事記3 - 描述',
            'bao_big_thing_date4':'寶寶大事記4 - 日期',
            'bao_big_thing_des4': '寶寶大事記4 - 描述',
            'bao_six_pic1': '閃蝦大家的寶照1',
            'bao_six_pic2' : '閃蝦大家的寶照2',
            'bao_six_pic3' : '閃蝦大家的寶照3',
            'bao_six_pic4' : '閃蝦大家的寶照4',
            'bao_six_pic5': '閃蝦大家的寶照5' ,
            'bao_six_pic6' : '閃蝦大家的寶照6'
        }
