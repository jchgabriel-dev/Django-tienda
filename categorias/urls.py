from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.listCategory.as_view(),name='listCategory'),
    path('addCategory/',views.addCategory.as_view(),name='addCategory'),
    path('deleteCategory/<int:pk>/',views.deleteCategory.as_view(),name='deleteCategory'),
    path('updateCategory/<int:pk>/',views.updateCategory.as_view(),name='updateCategory'),

]
