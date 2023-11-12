from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
import iyzipay
import json
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import requests
import pprint
from django.core.cache import cache
from LMSuser.models import CustomUser
from django.db.models import Q

#denemelms@gmail.com 102030

# Create your views here.

api_key = 'sandbox-7dsoIH0X8k42kMax2KTTPN0jnbWTlYm2'
secret_key = 'sandbox-nYM3GfqHKA0SG0RcMqumTANPZxKP8tOQ'
base_url = 'sandbox-api.iyzipay.com'


options = {
    'api_key': api_key,
    'secret_key': secret_key,
    'base_url': base_url
}
sozlukToken = list()

def payment(request):
    context = dict()
    kullanici = request.user
    odeme = Odeme.objects.get(user = kullanici, odendiMi = False)
    fiyat = odeme.total

    buyer={
        'id': 'BY789',
        'name': kullanici.first_name,
        'surname': kullanici.last_name,
        'gsmNumber': kullanici.phone_number,
        'email': kullanici.email,
        'identityNumber': kullanici.tc,
        'lastLoginDate': str(kullanici.last_login),
        'registrationDate': '2013-04-21 15:12:09',
        'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'ip': '85.34.78.112',
        'city': 'Istanbul',
        'country': 'Turkey',
        'zipCode': '34732'
    }

    address={
        'contactName': 'Jane Doe',
        'city': 'Istanbul',
        'country': 'Turkey',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'zipCode': '34732'
    }

    basket_items=[
        {
            'id': 'BI101',
            'name': 'Binocular',
            'category1': 'Collectibles',
            'category2': 'Accessories',
            'itemType': 'PHYSICAL',
            'price': '0.3'
        },
        {
            'id': 'BI102',
            'name': 'Game code',
            'category1': 'Game',
            'category2': 'Online Game Items',
            'itemType': 'VIRTUAL',
            'price': '0.5'
        },
        {
            'id': 'BI103',
            'name': 'Usb',
            'category1': 'Electronics',
            'category2': 'Usb / Cable',
            'itemType': 'PHYSICAL',
            'price': '0.2'
        }
    ]

    request={
        'locale': 'tr',
        'conversationId': '123456789',
        'price': '1',
        'paidPrice': int(fiyat),
        'currency': 'TRY',
        'basketId': 'B67832',
        'paymentGroup': 'PRODUCT',
        "callbackUrl": "http://127.0.0.1:8000/result/",
        "enabledInstallments": ['2', '3', '6', '9'],
        'buyer': buyer,
        'shippingAddress': address,
        'billingAddress': address,
        'basketItems': basket_items,
        # 'debitCardAllowed': True
    }

    checkout_form_initialize = iyzipay.CheckoutFormInitialize().create(request, options)

    #print(checkout_form_initialize.read().decode('utf-8'))
    page = checkout_form_initialize
    header = {'Content-Type': 'application/json'}
    content = checkout_form_initialize.read().decode('utf-8')
    json_content = json.loads(content)
    print(type(json_content))
    print(json_content["checkoutFormContent"])
    print("************************")
    print(json_content["token"])
    token = json_content['token']
    cache.set('token', token)
    print("************************")
    sozlukToken.append(json_content["token"])
    return HttpResponse(f'<div id="iyzipay-checkout-form" class="responsive">{json_content["checkoutFormContent"]}</div>')


@require_http_methods(['POST'])
@csrf_exempt
def result(request):
    context = dict()

    url = request.META.get('index')
    token =cache.get('token')

    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'token': token
    }
    checkout_form_result = iyzipay.CheckoutForm().retrieve(request, options)
    print("************************")
    print(type(checkout_form_result))
    result = checkout_form_result.read().decode('utf-8')
    print("************************")
    print(sozlukToken[0])   # Form oluşturulduğunda 
    print("************************")
    print("************************")
    sonuc = json.loads(result, object_pairs_hook=list)
    #print(sonuc[0][1])  # İşlem sonuç Durumu dönüyor
    #print(sonuc[5][1])   # Test ödeme tutarı
    print("************************")
    for i in sonuc:
        print(i)
    print("************************")
    print(sozlukToken)
    print("************************")
    if sonuc[0][1] == 'success':
        context['success'] = 'Başarılı İŞLEMLER'
        return HttpResponseRedirect(reverse('success'), context)

    elif sonuc[0][1] == 'failure':
        context['failure'] = 'Başarısız'
        return HttpResponseRedirect(reverse('failure'), context)

    return HttpResponse(url)



def success(request):
    odeme = Odeme.objects.get(user = request.user, odendiMi = False)
    odeme.odendiMi = True
    odeme.save()
    sepetim = Sepet.objects.filter(ekleyen = request.user, odendiMi = False)
    for i in sepetim:
        i.odendiMi = True
        i.save()
    messages.success(request,'Ödeme başarılı.')
    return redirect('indexPage')


def fail(request):
    messages.error(request, 'Ödeme başarısız. Yeniden deneyin.')
    return redirect('sepet')




def index(request):
    return render(request,'index.html')

def hakkimizda(request):
    egitmenler = CustomUser.objects.filter(is_teacher = True)
    context = dict(
        egitmenler = egitmenler
    )
    return render(request,'hakkimizda.html',context)

def iletisim(request):
    return render(request,'iletisim.html')


def egitimlerimiz(request):
    # anacategory = AnaCategory.objects.all()
    # altcategory = AltCategory.objects.all() 
    anacategory = AnaCategory.objects.filter(category__alt_category_name = 'HTML')

    print(anacategory)
    # anacategory.ana_category_set.all()
    
    # for i in anacategory:
    #     altcategory = AltCategory.objects.filter(ana_category = i.id)
    #     print(i,altcategory)
        


    context = dict(
        anacategory = AnaCategory.objects.all()
    )
    return render(request,'egitimlerimiz.html', context)

# def egitimlerimiz(request):
#     altcategory = AltCategory.objects.all() 
#     return render(request,'egitimlerimiz.html', {'altcategory' : altcategory})


def search(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        dersler = Egitimler.objects.filter(Q(egitimler_title__icontains = search)|
                                           Q(egitmen__first_name__icontains = search) |
                                           Q(egitmen__last_name__icontains = search))
        for i in dersler:
            print(i.egitimler_title)
        
        context = {
            'dersler':dersler ,
            'search':search
        }
    return render(request, 'search.html',context)

def sepet(request):
    if request.user.is_authenticated:
        kurslar = Sepet.objects.filter(ekleyen = request.user, odendiMi = False)
        toplam=0
        for i in kurslar:
            toplam +=i.total
        if request.method == 'POST':
            if 'odeme' not in request.POST:
                sepetId = request.POST['sepetId']
                sepet = Sepet.objects.get(id = sepetId)
            if 'sil' in request.POST:
                sepet.delete()
                messages.success(request, 'Eğitim silindi.')
                return redirect('sepet')
            elif 'odeme' in request.POST:
                if not Odeme.objects.filter(user = request.user, odendiMi = False).exists():
                    odeme = Odeme.objects.create(
                        user = request.user,
                        total = toplam
                    )
                    odeme.egitimler.add(*kurslar)
                    odeme.save()
                return redirect('payment')

        
        context = {
            'kurslar':kurslar,
            'toplam':toplam
        }
        return render(request,'sepet.html',context)
    return render(request,'sepet.html')
    

def dersler(request, category_slug):
    dersler = Egitimler.objects.filter(egitim_alt_kategori__slug = category_slug)
    if request.method == "POST":
        if request.user.is_authenticated:
            egitimId = request.POST['egitimId']
            dersim = Egitimler.objects.get(id = egitimId)
            if Sepet.objects.filter(ekleyen = request.user, egitim = dersim, odendiMi=False).exists():
                sepet = Sepet.objects.get(ekleyen = request.user, egitim = dersim, odendiMi=False)
                sepet.total = dersim.egitim_ucreti
                sepet.save()
                
            else:
                sepet = Sepet.objects.create(
                    ekleyen = request.user,
                    egitim = dersim,
                    total = dersim.egitim_ucreti
                )
                sepet.save()
            return redirect('sepet')
        else:
            messages.warning(request, "Lütfen Giriş Yapınız")
            return redirect('login')


    return render(request,'dersler.html',{'dersler':dersler})




def egitmen(request, egitmen_id, slug):
    print(egitmen_id)
    dersler = Egitimler.objects.filter(egitmen_id = egitmen_id)
    egitmen = CustomUser.objects.get(pk = egitmen_id)
    ders_sayisi = dersler.count()
    if request.method == "POST":
        if request.user.is_authenticated:
            egitimId = request.POST['egitimId']
            dersim = Egitimler.objects.get(id = egitimId)
            if Sepet.objects.filter(ekleyen = request.user, egitim = dersim, odendiMi=False).exists():
                sepet = Sepet.objects.get(ekleyen = request.user, egitim = dersim, odendiMi=False)
                sepet.total = dersim.egitim_ucreti
                sepet.save()
                
            else:
                sepet = Sepet.objects.create(
                    ekleyen = request.user,
                    egitim = dersim,
                    total = dersim.egitim_ucreti
                )
                sepet.save()
            return redirect('sepet')
        else:
            messages.warning(request, "Lütfen Giriş Yapınız")
            return redirect('login')
    context = {
        'dersler' : dersler,
        'egitmen' : egitmen,
        'ders_sayisi':ders_sayisi
    }
    return render(request,'egitmen.html', context)





def instructor(request):
    return render(request,'instructor.html')

def mesajlar(request):
    return render(request,'mesajlar.html')

def ogrenciLogin(request):
    odemeler = Odeme.objects.filter(user=request.user, odendiMi = True)
    context = {
        'odemeler':odemeler
    }
    return render(request,'ogrenciLogin.html',context)


@login_required(login_url='login')
def videoPlayer(request, egitim_id):
    video = get_object_or_404(Egitimler, id=egitim_id)
    odeme_var_mi = Sepet.objects.filter(ekleyen=request.user, odendiMi=True, egitim=video).exists()

    if odeme_var_mi:
        videolar = Video_player.objects.filter(video_egitim_id=egitim_id)
        context = {
            'videolar': videolar,
            'video_egitim': video,
        }
        return render(request, 'videoPlayer.html', context)
    else:
        return HttpResponse("Bu videoyu izlemek için ödeme yapmalısınız.")


# @login_required(login_url='login')
# def videoPlayer(request,egitim_id):
#     odemeler = Odeme.objects.filter(user=request.user, odendiMi = True, egitimler = video)
#     if odemeler.odendiMi==True:
#         video=get_object_or_404(Egitimler,id=egitim_id)
#         videolar = Video_player.objects.filter(video_egitim_id=egitim_id)
#         context = {
#             'videolar':videolar,
#             'video_egitim':video,
#             'odemeler':odemeler

#         }
#     return render(request,'videoPlayer.html', context)

@login_required(login_url='login')
def kursOlustur(request):
        if request.user.is_teacher == True:
            if request.method == 'POST':
                courseForm = CreateCourseForm(request.POST, request.FILES)
                if courseForm.is_valid():
                    egitimler_title = courseForm.cleaned_data['egitimler_title']
                    slug = slugify(egitimler_title),


                    new_course = Egitimler(
                        egitimler_title = egitimler_title,
                        egitim_icerigi = courseForm.cleaned_data['egitim_icerigi'],
                        egitim_alt_kategori =courseForm.cleaned_data['egitim_alt_kategori'],
                        egitim_seviyesi = courseForm.cleaned_data['egitim_seviyesi'],
                        egitim_suresi = courseForm.cleaned_data['egitim_suresi'],
                        egitim_ucreti = courseForm.cleaned_data['egitim_ucreti'],
                        egitim_image = courseForm.cleaned_data['egitim_image'],
                        egitmen = request.user,
                        slug = slug
                    )

                    new_course.save()

                    # for kategori in courseForm.cleaned_data['egitim_ana_kategori']:
                    #     new_course.egitim_ana_kategori.add(kategori)

                    messages.success(request, 'Kurs oluşturuldu')
                
                else:
                    print(courseForm.errors) 

                    return redirect('indexPage')
            else:
                courseForm = CreateCourseForm()

        else: 
            messages.error(request, 'Kurs oluşturmak için yetkili değilsiniz.')

            return redirect('indexPage')
        
        context = {
            'courseForm':courseForm
        }
        return render(request, 'kursOlustur.html', context)

@login_required(login_url='login')
def videoUpload(request,egitmen_id):
    dersler = Egitimler.objects.filter(egitmen_id = egitmen_id)
    egitmen=get_object_or_404(CustomUser, id = egitmen_id)
    if request.user.id == egitmen_id:
        if request.user.is_teacher == True:
            if request.method == 'POST':
                videoForm = CreateVideoForm(request.POST)
                if videoForm.is_valid():
                    new_video = Video_player(
                        video_player_title = videoForm.cleaned_data['video_player_title'],
                        video_aciklama = videoForm.cleaned_data['video_aciklama'],
                        video_suresi = videoForm.cleaned_data['video_suresi'],
                        video_id = videoForm.cleaned_data['video_id'],
                        video_egitim = videoForm.cleaned_data['video_egitim'],
                    )

                    new_video.save()

                    return redirect('indexPage')
            else:
                videoForm = CreateVideoForm()

        else:     
            messages.error(request, 'Video yüklemek için yetkili değilsiniz.')

            return redirect('indexPage')
            
        context = {
            'videoForm':videoForm,
            'dersler':dersler,
            'egitmen':egitmen,
            'user':request.user

        }

        return render(request,'videoUpload.html', context)
    

def view_404(request, exception):
    return redirect('/')


def view_500(request):
    return render(request, 'hata.html')

# @login_required(login_url='login')
# def videoUpload(request, egitmen_id):
#     egitmen = get_object_or_404(CustomUser, pk=egitmen_id)
#     kurslarım = Egitimler.objects.filter(egitmen_id = egitmen_id)
#     if request.user.is_teacher == True:
#         if request.method == 'POST':
#             videoForm = CreateVideoForm(request.POST)
#             if videoForm.is_valid():
#                 new_video = Video_player(
#                     video_player_title = videoForm.cleaned_data['video_player_title'],
#                     video_aciklama = videoForm.cleaned_data['video_aciklama'],
#                     video_suresi = videoForm.cleaned_data['video_suresi'],
#                     video_id = videoForm.cleaned_data['video_id'],
#                     video_egitim = videoForm.cleaned_data['video_egitim'],
#                 )

#                 new_video.save()

#                 return redirect('indexPage')
#         else:
#             videoForm = CreateVideoForm()

#     else:     
#         messages.error(request, 'Video yüklemek için yetkili değilsiniz.')

#         return redirect('indexPage')
        
#     context = {
#         'videoForm':videoForm,
#         'kurslarım':kurslarım
#     }

#     return render(request,'videoUpload.html', context)
