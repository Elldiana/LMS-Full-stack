from django.urls import path
from .views import *
urlpatterns = [
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('forgetpass/',forgetpass,name='forgetpass'),
    path('changermotdepasse/',changermotdepasse,name='changermotdepasse'),
    path('editProfile/',edit_profile,name='editProfile'),
    path('logout/',logout_request,name='logout'),

]