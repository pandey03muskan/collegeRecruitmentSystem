from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('contactus/', views.contactus),
    path('newvacancy/', views.newvacancy),
    path('appliedjobs/', views.appliedjobs),
    path('placement/', views.placement),
    path('registration/', views.registration),
    path('myprofile/', views.myprofile),
    path('adminlogin/', views.adminlogin),
    path('termcondition/', views.termcondition),
    path('privacypolicy/', views.privacypolicy),
]