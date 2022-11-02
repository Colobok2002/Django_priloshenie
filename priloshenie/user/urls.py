from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path(r'^sign_in/$', views.login),
    re_path(r'reg/',views.register),
    re_path(r'logout/',views.logout),
    re_path(r'reg_sing/',views.reg_sing),

]
