from django.shortcuts import render, get_object_or_404, redirect
from .form import productForm
from .models import Producto
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .utils import render_to_pdf 

# Create your views here.

class listProduct(ListView):
	model = Producto
	template_name = 'productos/listProduct.html'
	queryset = Producto.objects.all()

class addProduct(CreateView):
	model = Producto
	template_name = 'productos/addProduct.html'
	form_class = productForm
	success_url = reverse_lazy('listProduct')

class deleteProduct(DeleteView):
	model = Producto
	success_url = reverse_lazy('listProduct')

class updateProduct(UpdateView):
	model = Producto
	template_name = 'productos/updateProduct.html'
	form_class = productForm
	success_url = reverse_lazy('listProduct')

class listProductPDF(View):
	def get(self, request, *args, **kwargs):
		products = Producto.objects.all()
		data = {
			'products' : products
		}
		pdf = render_to_pdf('productos/tablaProductos.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf') 
