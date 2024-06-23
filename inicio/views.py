from django.shortcuts import render 
from productos.models import Producto
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from cuentas.models import Client, Adm
from productos.models import Producto
from categorias.models import Categoria
from proveedores.models import Proveedor
from pedidos.models import Venta

# Create your views here.

def Inicio(request):
	return render(request, 'Inicio/inicio.html')

def Contactos(request):
	return render(request, 'Inicio/contactos.html')

def Administracion(request):
	countC = Categoria.objects.all().count()
	countP = Proveedor.objects.all().count()
	countR = Producto.objects.all().count()
	countA = Adm.objects.all().count()
	countL = Client.objects.all().count()
	countV = Venta.objects.all().count()
	context = {'countV':countV,'countL':countL,'countA':countA, 'countC':countC, 'countP':countP, 'countR': countR}
	return render(request, 'Inicio/administracion.html',context)

class inventario(ListView):
	model = Producto
	template_name = 'Inicio/inventario.html'
	queryset = Producto.objects.all()

