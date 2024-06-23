from django.shortcuts import render, get_object_or_404, redirect
from productos.models import Producto
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from .form import MovForm
from .models import Movimiento

# Create your views here.


def movimientos(request):
	context = {
		'prods' : Producto.objects.all(),

	}	
	return render(request, 'movimientos/inventory.html',context)

def update(request, pk):
	pro = Producto.objects.get(id=pk)
	form = MovForm(request.POST)
	if form.is_valid(): 
		mov = form.save()
		mov.prod=pro
		mov.save()
		if mov.entry == 1:
			pro.units += mov.quant
		else:
			pro.units -= mov.quant
		pro.save()
		return redirect('movimientos')

	context = {'form':form}
	return render(request, 'movimientos/create.html', context)	

class registro(ListView):
	model = Movimiento
	template_name = 'movimientos/list.html'
	queryset = Movimiento.objects.all()