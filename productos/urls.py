from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.listProduct.as_view(),name='listProduct'),
    path('addProduct/',views.addProduct.as_view(),name='addProduct'),
    path('deleteProduct/<int:pk>/',views.deleteProduct.as_view(),name='deleteProduct'),
    path('updateProduct/<int:pk>/',views.updateProduct.as_view(),name='updateProduct'),
    path('listProductPDF/',views.listProductPDF.as_view(),name='listProductPDF'),

]
