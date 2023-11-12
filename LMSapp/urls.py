from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='indexPage'),
    path('hakkimizda/',hakkimizda,name='hakkimizda'),
    path('iletisim/',iletisim,name='iletisim'),
    path('egitimlerimiz/',egitimlerimiz,name='egitimlerimiz'),
    path('sepet/',sepet,name='sepet'),
    path('egitimlerimiz/<slug:category_slug>',dersler,name='dersler'),
    path('egitmen/<int:egitmen_id>/<slug:slug>',egitmen,name='egitmen'),
    path('search/',search,name='search'),
    path('mesajlar/',mesajlar,name='mesajlar'),
    path('derslerim/',ogrenciLogin,name='ogrenciLogin'),
    path('videoPlayer/<int:egitim_id>',videoPlayer,name='videoPlayer'),
    path('kursOlustur/',kursOlustur,name='kursOlustur'),
    path('videoUpload/<int:egitmen_id>',videoUpload,name='videoUpload'),
    path('payment/', payment, name='payment'),
    path('result/', result, name='result'),
    path('success/', success, name='success'),
    path('failure/', fail, name='failure'),
]

