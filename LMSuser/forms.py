from django import forms
from .models import *
from django.forms import widgets


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=64,
        widget=forms.EmailInput(attrs={
            'class': 'm-auto relative bg-gray-50 ring-0 outline-none border border-neutral-500 text-neutral-900 placeholder-mor text-sm rounded-lg focus:ring-mor focus:border-mor block w-64 p-2.5 checked:bg-emerald-500',
            'placeholder': 'Mail Adresiniz...'
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'm-auto relative bg-gray-50 ring-0 outline-none border border-neutral-500 text-neutral-900 placeholder-mor text-sm rounded-lg focus:ring-mor focus:border-mor block w-64 p-2.5 checked:bg-emerald-500',
            'placeholder': '************'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email = email).exists():
            self.add_error('email','Bu email adresi kayıtlı değil.')
        return email

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'tc', 'phone_number', 'is_teacher']

        labels = {
            'first_name': 'Ad',
            'last_name': 'Soyad',
            'email': 'Email',
            'password': 'Şifre',
            'tc': 'Tc Kimlik No',
            'phone_number': 'Telefon Numarası',
            'is_teacher': 'Öğretmen mi?',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'm-auto relative bg-gray-50 ring-0 outline-none border border-neutral-500 text-neutral-900 placeholder-mor text-sm rounded-lg focus:ring-mor focus:border-mor block p-2.5 w-60 checked:bg-emerald-500' , 'placeholder': 'Ad'}),

            'last_name': forms.TextInput(attrs={'class': 'm-auto relative bg-gray-50 ring-0 outline-none border border-neutral-500 text-neutral-900 placeholder-mor text-sm rounded-lg focus:ring-mor focus:border-mor block p-2.5 w-60 checked:bg-emerald-500','placeholder': 'Soyad'}),

            'email': forms.EmailInput(attrs={'class': 'm-auto relative bg-gray-50 ring-0 outline-none border border-neutral-500 text-neutral-900 placeholder-mor text-sm rounded-lg focus:ring-mor focus:border-mor block p-2.5 w-60 checked:bg-emerald-500','placeholder': 'Mail Adresiniz...'}),

            'password': forms.PasswordInput(attrs={'class': 'm-auto relative bg-gray-50 ring-0 outline-none border border-neutral-500 text-neutral-900 placeholder-mor text-sm rounded-lg focus:ring-mor focus:border-mor block w-60 p-2.5 checked:bg-emerald-500','placeholder': '******'}),

            'tc': forms.TextInput(attrs={'class': 'm-auto relative bg-gray-50 ring-0 outline-none border border-neutral-500 text-neutral-900 placeholder-mor text-sm rounded-lg focus:ring-mor focus:border-mor block w-60 p-2.5 checked:bg-emerald-500','placeholder':'Tc No Giriniz'}),

            'phone_number': forms.TextInput(attrs={'class': 'm-auto relative bg-gray-50 ring-0 outline-none border border-neutral-500 text-neutral-900 placeholder-mor text-sm rounded-lg focus:ring-mor focus:border-mor block w-60 p-2.5 checked:bg-emerald-500','placeholder':'Telefon Numaranız'}),
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='Mevcut Şifreniz', widget=forms.PasswordInput(attrs={'class': 'mb-7 bg-lacivert opacity-90 shadow-xl text-white w-full box-border pt-[12px] pr-[36px] pb-[12px] pl-[12px] rounded-lg px-4 py-3 focus:outline-none focus:ring-1 focus:ring-gray-100 focus:ring-offset-1 focus:ring-offset-gray-600 placeholder-gray-300', 'placeholder': 'Mevcut Şifreniz'}))
    new_password = forms.CharField(label='Yeni Şifreniz', widget=forms.PasswordInput(attrs={'class': 'mb-7 bg-lacivert opacity-90 shadow-xl text-white w-full rounded-lg px-4 py-3 focus:outline-none focus:ring-1 focus:ring-gray-100 focus:ring-offset-1 focus:ring-offset-gray-600 placeholder-gray-300', 'placeholder': 'Yeni Şifreniz'}))
    confirm_password = forms.CharField(label='Yeni Şifre (Tekrar)', widget=forms.PasswordInput(attrs={'class': 'bg-lacivert opacity-90 shadow-xl text-white w-full rounded-lg px-4 py-3 focus:outline-none focus:ring-1 focus:ring-gray-100 focus:ring-offset-1 focus:ring-offset-gray-600 placeholder-gray-300', 'placeholder': 'Yeni Şifre (Tekrar)'}))

class EditProfileForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'w-full py-2 px-3 border border-gray-300 rounded focus:outline-none focus:border-blue-400',})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'w-full py-2 px-3 border border-gray-300 rounded focus:outline-none focus:border-blue-400',})
    )
    tc = forms.CharField(
        widget=forms.TextInput(attrs={'class':'w-full py-2 px-3 border border-gray-300 rounded focus:outline-none focus:border-blue-400',})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class':'w-full py-2 px-3 border border-gray-300 rounded focus:outline-none focus:border-blue-400',})
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class':'w-full py-2 px-3 border border-gray-300 rounded focus:outline-none focus:border-blue-400',})
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class':'resize-none w-full py-2 px-3 border border-gray-300 rounded focus:outline-none focus:border-blue-400'})
    )
    # Diğer alanlar için aynı şekilde devam edebilirsiniz

class EditImageForm(forms.Form):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'py-2 px-2 text-sm text-white mb-4 rounded border border-gray-300 focus:outline-none focus:border-blue-400'}),
    )
