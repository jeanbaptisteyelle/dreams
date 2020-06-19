from django.contrib import admin
from . import models
from application import models as application_models
# Register your models here.

@admin.Register(models.About)
class AboutAdmin(admin.ModelsAdmin):
    list_display = ('titre','date_update','date_add','status','image_view')

@admin.Register(models.Siteinfo)
class SiteinfoAdmin(admin.ModelsAdmin):
    list_display = ()
@admin.Register(models.Contact)
class ContactAdmin(admin.ModelsAdmin):

@admin.Register(models.Newletter)
class NewletterAdmin(admin.ModelsAdmin):

@admin.Register(models.Reseau_social)
class Reseau_social(admin.ModelsAdmin):
