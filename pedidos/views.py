from django.shortcuts import render, redirect
from .form import PedForm
from productos.models import Producto
from .models import Pedido, Venta
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy 


# Create your views here.

def checkout(request, pk):
	ped = Pedido.objects.get(id=pk)
	context = {'ped':ped}
	if request.method == 'POST':
		ven = Venta.objects.create()
		ven.ped = ped
		ven.user = request.user.client
		ven.save()
		pro = ped.item
		pro.units -= ped.quantity
		pro.save()
		ped.pay = True
		ped.save()
		return redirect('Inicio')

	return render(request, 'pedidos/checkout.html', context)

def pedidos(request, pk):
	pro = Producto.objects.get(id=pk)
	form = PedForm(request.POST)
	if form.is_valid():
		ped = form.save()
		ped.user = request.user.client
		ped.item = pro
		print(ped.id)
		ped.save()
		return redirect('checkout', pk=ped.id)
		
	context = {'pro':pro,'form':form}
	return render(request, 'pedidos/pedido.html', context)	

class listVentas(ListView):
	model = Venta
	template_name = 'pedidos/listVentas.html'
	queryset = Venta.objects.all()

class listPed(ListView):
	model = Pedido
	template_name = 'pedidos/listPed.html'
	queryset = Pedido.objects.all()

	def get_queryset(self):
		return Pedido.objects.filter(
			user=self.request.user.client
		)

class deletePed(DeleteView):
	model = Pedido
	success_url = reverse_lazy('listPed')