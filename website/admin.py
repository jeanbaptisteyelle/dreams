from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('titre','date_update','date_add','status')

@admin.register(models.Siteinfo)
class SiteinfoAdmin(admin.ModelAdmin):
    list_display = ('slogan','phone','message','email','adresse','contact','date_add','date_update','status','mapping','logo','image',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom','email','date_add','date_update','status','sujet')

@admin.register(models.Newletter)
class NewletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_add','date_update','status')

@admin.register(models.Reseausocial)
class Reseausocial(admin.ModelAdmin):
    list_display = ('nom','lien','date_add','status','date_update')

@admin.register(models.Temoignage)
class Temoignage(admin.ModelAdmin):
    list_display = ('user','message','date_add','date_update','status')