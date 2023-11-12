from django.contrib import admin
from .models import *

@admin.register(Egitimler)
class EgitimlerAdmin(admin.ModelAdmin):
    list_display = ['egitimler_title',]
    readonly_fields=['slug',]


@admin.register(Video_player)
class Video_playerAdmin(admin.ModelAdmin):
    pass




@admin.register(Sepet)
class SepetAdmin(admin.ModelAdmin):
    def ekleyen_first_name(self, obj):
        return obj.ekleyen.first_name
    ekleyen_first_name.short_description = 'Ekleyen İsim'
    list_display = ['ekleyen_first_name', 'egitim', 'total', 'odendiMi']
    list_filter = ['ekleyen__first_name', 'egitim', 'odendiMi']



@admin.register(AnaCategory)
class AnaCategoryAdmin(admin.ModelAdmin):
    list_display = ['ana_category_name',]
    readonly_fields=['slug',]

@admin.register(AltCategory)
class AltCategoryAdmin(admin.ModelAdmin):
    list_display = ['alt_category_name',]
    readonly_fields=['slug',]   

@admin.register(CourseLevel)
class CourseLevelAdmin(admin.ModelAdmin):
    list_display = ['egitim_seviyesi',]    
    

@admin.register(Odeme)
class OdemeAdmin(admin.ModelAdmin):
    pass    