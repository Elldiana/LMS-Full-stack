from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class Rozetler(models.Model):
    image = models.ImageField(upload_to='rozet_pic')

def get_default_profile_image():
    return 'profile_pic/avatar.png'

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_pic', null=True, blank=True, default=get_default_profile_image, verbose_name='Profil Resmi')
    phone_number = models.CharField(max_length=11, null=True)
    tc = models.CharField(max_length=11, null=True)
    is_teacher = models.BooleanField(default=False)
    password = models.CharField(max_length=128)
    description = models.TextField(null=True)
    rozet = models.ManyToManyField(Rozetler)
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True, editable=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name+'-'+self.last_name)
        super().save(*args, **kwargs)



