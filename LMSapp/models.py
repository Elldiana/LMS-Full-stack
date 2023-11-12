from django.db import models
from LMSuser.models import *
from django.utils.text import slugify
# Create your models here.


class AnaCategory(models.Model):
    ana_category_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True, editable=False)
    

    def __str__(self):
        return self.ana_category_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.ana_category_name)
        super().save(*args, **kwargs)

class AltCategory(models.Model):
    alt_category_name = models.CharField(max_length=100)
    alt_category_image = models.ImageField(upload_to='category_pic')
    ana_category = models.ManyToManyField(AnaCategory, related_name='category')
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True, editable=False)


    def __str__(self):
        return self.alt_category_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.alt_category_name)
        super().save(*args, **kwargs)


class CourseLevel(models.Model):
    egitim_seviyesi = models.CharField(max_length=50)

    def __str__(self):
        return self.egitim_seviyesi


class Egitimler(models.Model):
    egitimler_title = models.CharField(max_length=200)
    egitim_icerigi = models.CharField(max_length=200)
    egitim_suresi = models.IntegerField()
    egitim_ana_kategori = models.ManyToManyField(AnaCategory, blank= True, null=True)
    egitim_alt_kategori = models.ForeignKey(AltCategory, on_delete= models.SET_NULL, null= True)
    egitim_image = models.ImageField(upload_to='egitim_pic')
    egitim_seviyesi = models.ForeignKey(CourseLevel,on_delete=models.SET_NULL, null=True)
    egitim_ucreti = models.IntegerField(null=True)
    egitmen = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.egitimler_title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.egitimler_title)
        super().save(*args, **kwargs)


class Video_player(models.Model):
    video_player_title = models.CharField(max_length=50)
    video_aciklama = models.TextField(max_length=300)
    video_suresi = models.IntegerField()
    video_id = models.CharField(max_length=255, null=True)
    video_egitmen = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    video_egitim = models.ForeignKey(Egitimler, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.video_player_title





class Sepet(models.Model):
    ekleyen = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    egitim = models.ForeignKey(Egitimler, on_delete=models.CASCADE)
    total = models.IntegerField()
    odendiMi = models.BooleanField(default=False, verbose_name='Ödendi mi?')
    

    def __str__(self):
        return self.egitim.egitimler_title
    
class Odeme(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    egitimler = models.ManyToManyField(Sepet)
    total = models.IntegerField()
    odendiMi = models.BooleanField(default=False)
    odeme_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
