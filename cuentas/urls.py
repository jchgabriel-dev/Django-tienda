from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('registerClient/',views.registerClient.as_view(),name='registerClient'),
    path('registerAdmin/',views.registerAdmin.as_view(),name='registerAdmin'),
    path('loginUser/',views.loginUser,name='loginUser'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('listAdmin/',views.listAdmin.as_view(), name='listAdmin'),
    path('profileadm/', views.profileadm, name='profileadm'),
    path('profilecli/', views.profilecli, name='profilecli'),
    path('password/', views.password, name="password")

]
