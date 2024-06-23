from django.db import models
from productos.models import Producto

# Create your models here.
 
type_entry = [
    (1, "Entrada"),
    (2, "Salida"),
]
class Movimiento(models.Model):
    prod = models.ForeignKey(Producto, on_delete = models.SET_NULL, null=True)
    entry = models.IntegerField(
        null=False, blank=False,
		choices=type_entry,
		default=1,
    )
    quant = models.IntegerField()