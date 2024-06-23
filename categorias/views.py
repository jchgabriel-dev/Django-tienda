from django.shortcuts import render, get_object_or_404, redirect
from .form import categoryForm
from .models import Categoria
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy 

# Create your views here.

class listCategory(ListView):
	model = Categoria
	template_name = 'categorias/listCategory.html'
	queryset = Categoria.objects.all()

class addCategory(CreateView):
	model = Categoria
	template_name = 'categorias/addCategory.html'
	form_class = categoryForm
	success_url = reverse_lazy('addCategory')

class deleteCategory(DeleteView):
	model = Categoria
	success_url = reverse_lazy('listProduct')

class updateCategory(UpdateView):
	model = Categoria
	template_name = 'categorias/updateCategory.html'
	form_class = categoryForm
	success_url = reverse_lazy('listProduct')
