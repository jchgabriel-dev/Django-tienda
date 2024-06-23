from django.db import models
from categorias.models import Categoria
from proveedores.models import Proveedor
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Producto(models.Model):
	product_status = [
		(1,"Disponible"),
		(2,"Not disponible"),
	]
	barcode = models.IntegerField()
	name = models.CharField(max_length=20)
	units = models.IntegerField(default=0)
	price = models.IntegerField()
	cat = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null=True)
	prov = models.ForeignKey(Proveedor, on_delete = models.SET_NULL, null=True)
	stat = models.IntegerField(
		null=False, blank=False,
		choices=product_status,
		default=1,
		)
	img = models.ImageField(upload_to='pics')

	def __str__(self):
		return self.name
