from django.db import models
from productos.models import Producto
from cuentas.models import Client

# Create your models here.

class Pedido(models.Model):
	user = models.ForeignKey(Client, on_delete=models.CASCADE,null=True,blank=True)
	item = models.ForeignKey(Producto, on_delete=models.CASCADE,null=True,blank=True)
	quantity = models.IntegerField(default=1)
	pay = models.BooleanField(default=False)
	
	def get_price(self):
		return self.quantity * self.item.price

class Venta(models.Model):
	user = models.ForeignKey(Client, on_delete=models.CASCADE,null=True,blank=True)
	ped = models.ForeignKey(Pedido, on_delete=models.CASCADE,null=True,blank=True)

