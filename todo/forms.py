from django import forms
from .models import Todo,Customer,Flight
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget



class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'name', 'finish')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '待辦事項'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '待辦事項'})
        }

class FlightModelForm(forms.ModelForm):
    """docstring for FlightModelForm"""
    
    class Meta:
        model = Flight
        fields = ( 'items', 'fromname', 'arrivalname', 'description', 'pd_number','pd_content','pd_weight','pd_profit')
        widgets = {
            'items': forms.Select(choices=(('', '請選擇'),) + Flight.items_choices, attrs={'class': 'form-control'}),
            'fromname': forms.TextInput(attrs={'class': 'form-control','rows':'4'}),
            'arrivalname': forms.TextInput(attrs={'class': 'form-control','rows':'4'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'rows': '4'}),
            'pd_number': forms.TextInput(attrs={'class': 'form-control', 'rows': '4'}),
            'pub_date': forms.TextInput(attrs={'class': 'form-control', 'rows': '4'}),
            'pd_weight': forms.TextInput(attrs={'class': 'form-control', 'rows': '4'}),
            'pd_profit': forms.TextInput(attrs={'class': 'form-control', 'rows': '4'}),

        }



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
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )        

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'style':'width:20%'})
        }
        labels = {
            'name': '姓名',
            'email': '電子郵件',
            'tel': '聯絡電話',
            'password':'密碼',
        }    






