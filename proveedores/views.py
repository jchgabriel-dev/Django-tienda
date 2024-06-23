from django.shortcuts import render, get_object_or_404, redirect
from .form import providerForm
from .models import Proveedor
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class listProvider(ListView):
	model = Proveedor
	template_name = 'proveedores/listProvider.html'
	queryset = Proveedor.objects.all()

class addProvider(CreateView):
	model = Proveedor
	template_name = 'proveedores/addProvider.html'
	form_class = providerForm
	success_url = reverse_lazy('listProduct')

class deleteProvider(DeleteView):
	model = Proveedor
	success_url = reverse_lazy('listProduct')

class updateProvider(UpdateView):
	model = Proveedor
	template_name = 'proveedores/updateProvider.html'
	form_class = providerForm
	success_url = reverse_lazy('listProduct')
