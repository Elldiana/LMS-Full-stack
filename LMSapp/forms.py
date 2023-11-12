from django import forms
from .models import *

class CreateCourseForm(forms.Form):
    egitimler_title = forms.CharField(
        widget=forms.TextInput(attrs={'class':'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2',
                                      'placeholder':'Kurs başlığını girin'})
    )
    egitim_icerigi = forms.CharField(
        widget=forms.TextInput(attrs={'class':'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2',
                                      'placeholder':'Kurs içeriğini girin'})
    )
    egitim_ana_kategori = forms.ModelMultipleChoiceField(
        queryset=AnaCategory.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2',
                                   }),
    )
    egitim_alt_kategori = forms.ModelChoiceField(
        queryset=AltCategory.objects.all(),
        widget=forms.Select(attrs={'class': 'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2'}),
        empty_label="Kurs alt kategorisini seçin"
    )
    egitim_seviyesi = forms.ModelChoiceField(
        queryset=CourseLevel.objects.all(),
        widget=forms.Select(attrs={'class': 'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2'}),
        empty_label="Kurs seviyesini seçin"
    )
    egitim_suresi = forms.CharField(
        widget=forms.TextInput(attrs={'class':'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2',
                                      'placeholder':'Kurs süresini girin'})
    )
    egitim_ucreti = forms.CharField(
        widget=forms.TextInput(attrs={'class':'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2',
                                      'placeholder':'Kurs ücretini girin'})
    )
    egitim_image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'course-input text-white mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2'}),
        required=True,
    )

class CreateVideoForm(forms.Form):
    video_player_title = forms.CharField(
        widget=forms.TextInput(attrs={'class':'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2',
                                      'placeholder':'Video başlığını girin'})
    )
    video_aciklama = forms.CharField(
        widget=forms.TextInput(attrs={'class':'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2',
                                      'placeholder':'Video açıklamasını girin'})
    )
    video_suresi = forms.CharField(
        widget=forms.TextInput(attrs={'class':'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2',
                                      'placeholder':'Video süresini girin'})
    )
    video_id = forms.CharField(
        widget=forms.TextInput(attrs={'class':'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2',
                                      'placeholder':'Youtube video id girin'})
    )
    video_egitim = forms.ModelChoiceField(
        queryset=Egitimler.objects.all(),
        widget=forms.Select(attrs={'class': 'course-input mt-4 p-2 w-4/5 m-2 border rounded text-sm sm:text-base max-[400px]:w-1/2'}),
        empty_label="Kursu seçin"
    )
    