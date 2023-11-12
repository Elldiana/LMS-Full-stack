from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,authenticate, logout
from .models import CustomUser
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = CustomUser.objects.get(email=email).username
            user = authenticate(username = username, password = password)
           
            if user is not None:
                login(request, user)
                return redirect('indexPage')  # Giriş başarılıysa yönlendirme yapabilirsiniz
            else:
                messages.error(request, 'Giriş başarısız: Kullanıcı doğrulanamadı.')
    else:
        form = LoginForm()

    return render(request, 'login.html',{'form':form})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            tc = form.cleaned_data.get('tc')
            phone_number = form.cleaned_data.get('phone_number')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            is_teacher = form.cleaned_data.get('is_teacher')

            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                user = None
            if user is None:
                # Kullanıcıyı oluştur
                username = get_random_string(length=10) 
                user = CustomUser(email=email, username=username, first_name=first_name, last_name=last_name, tc=tc, phone_number=phone_number, is_teacher=is_teacher)
                user.set_password(password)
                user.save()

                # Kullanıcıyı kimlik doğrula
                authenticated_user = authenticate(request, username=user.username, password=password)
                login(request, authenticated_user)

                # Kayıt işlemi başarılı oldu.
                messages.success(request, 'Kayıt işlemi başarıyla tamamlandı.')
                return redirect('login')  # Başarılı kayıttan sonra yönlendirilecek URL
            else:
                messages.error(request, 'Bu e-posta zaten kullanılıyor.')
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})


# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             tc = form.cleaned_data.get('tc')
#             phone_number = form.cleaned_data.get('phone_number')
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('last_name')
#             is_teacher = form.cleaned_data.get('is_teacher')

#             try:
#                 user = CustomUser.objects.get(email=email)
#             except CustomUser.DoesNotExist:
#                 user = None
#             if user is None:
#                 # Kullanıcıyı oluştur
#                 username = get_random_string(length=10) 
#                 user = CustomUser(email=email, username=username, first_name=first_name, last_name=last_name,tc=tc,phone_number=phone_number,is_teacher=is_teacher)
#                 user.set_password(password)
#                 user.save()

#                 # Kullanıcıyı oturum açmış bir şekilde işaretle
#                 authenticated_user = authenticate(username=email, password=password)
#                 login(request, authenticated_user)

#                 # Kayıt işlemi başarılı oldu.
#                 messages.success(request, 'Kayıt işlemi başarıyla tamamlandı.')
#                 return redirect('indexPage')  # Başarılı kayıttan sonra yönlendirilecek URL
#             else:
#                 messages.error(request, 'Bu e-posta zaten kullanılıyor.')
#     else:
#         form = CustomUserForm()
#     return render(request, 'register.html', {'form': form})

def forgetpass(request):
    return render(request,'forgetpass.html')


def changermotdepasse(request):
    form = ChangePasswordForm()

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        try:
            if form.is_valid():
                current_password = form.cleaned_data['current_password']
                new_password = form.cleaned_data['new_password']
                confirm_password = form.cleaned_data['confirm_password']
                
                if not request.user.check_password(current_password):
                    messages.error(request, "Mevcut şifre yanlış.")
                    return render(request, 'changermotdepasse.html', {'form': form})

                # Yeni şifre ve doğrulama şifresi eşleşleştirme
                if new_password != confirm_password:
                    messages.error(request, "Yeni şifreler eşleşmiyor.")
                    return render(request, 'changermotdepasse.html', {'form': form})

                # Şifreyi güncelle
                request.user.set_password(new_password)
                request.user.save()

                update_session_auth_hash(request, request.user)
                messages.success(request, 'Şifreniz başarıyla değiştirildi.')
                return redirect('changermotdepasse')
        except Exception as e:
            messages.error(request, f'Hata oluştu: {e}')
            return render(request, 'changermotdepasse.html', {'form': form})
    return render(request, 'changermotdepasse.html', {'form': form})


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        if 'bilgi_kaydet' in request.POST:
            editForm = EditProfileForm(request.POST)
            if editForm.is_valid():
                user = request.user 
                user.first_name = editForm.cleaned_data['first_name']
                user.last_name = editForm.cleaned_data['last_name']
                user.email = editForm.cleaned_data['email']
                user.description = editForm.cleaned_data['bio']
                user.save()

                return redirect('indexPage')  

        if 'resim_kaydet' in request.POST:
            imageForm = EditImageForm(request.POST, request.FILES)

            if imageForm.is_valid():
                user = request.user
                user.image = imageForm.cleaned_data['image']
                user.save()
                
                return redirect('indexPage')
    else:
        user = request.user
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'tc':user.tc,
            'email': user.email,
            'phone_number':user.phone_number,
            'bio' : user.description
        }
        editForm = EditProfileForm(initial=initial_data)
        image_form = EditImageForm()
    
    return render(request, 'editProfile.html', {'editForm': editForm, 'imageForm':image_form})


def logout_request(request):
    logout(request)
    return redirect('indexPage')