from django.db import models

# Create your models here.

class Proveedor(models.Model):
	provider_status = [
		(1,"Activo"),
		(2,"Inactivo"),
	]
	persona = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 254)
	telefono = models.IntegerField()
	estado =  models.IntegerField(
		null=False, blank=False,
		choices=provider_status,
		default=1,
	)
	def __str__(self):
		return str(self.persona)