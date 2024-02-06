from django.contrib import admin

# Register your models here.
from .models import *
class contactAdmin(admin.ModelAdmin):
    list_display=("name","contact","email","message")
admin.site.register(contact,contactAdmin)

class companiesAdmin(admin.ModelAdmin):
    list_display=("id","cname","cpic","cdate","ccity","curl")
admin.site.register(companies,companiesAdmin)

class registerAdmin(admin.ModelAdmin):
    list_display=("name","dob","email","passwd","number","gender","address","qualification","course","year","resume","picture")
admin.site.register(register,registerAdmin)

class vacancyAdmin(admin.ModelAdmin):
    list_display=("cid","jid","designation","vacant","desc","skill","salary","vdate","clocation","ccompany")
admin.site.register(vacancy,vacancyAdmin)

class applyjobAdmin(admin.ModelAdmin):
    list_display = ("jid","sid")
admin.site.register(applyjob,applyjobAdmin)
# class registrationAdmin(admin.ModelAdmin):
#     list_display=("name","number","passwd","pro","dob","email")
# admin.site.register(registration,registrationAdmin)
# """class cmpdetailsAdmin(admin.ModelAdmin):
#     list_display=("id","cname","curl","clogo","cdate","citty")
# admin.site.register(cmpdetails,cmpdetailsAdmin)"""
# #addded
# """class placementAdmin(admin.ModelAdmin):
#     list_display=("id","pic","name","company")
# admin.site.register(placement,placementAdmin)"""