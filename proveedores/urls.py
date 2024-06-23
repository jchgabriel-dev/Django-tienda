from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.listProvider.as_view(),name='listProvider'),
    path('addProvider/',views.addProvider.as_view(),name='addProvider'),
    path('deleteProvider/<int:pk>/',views.deleteProvider.as_view(),name='deleteProvider'),
    path('updateProvider/<int:pk>/',views.updateProvider.as_view(),name='updateProvider'),

]
