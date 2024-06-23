from django import forms
from .models import Producto
from categorias.models import Categoria
from proveedores.models import Proveedor

class productForm(forms.ModelForm):
	
	class Meta:
		model = Producto
		fields = [
			'barcode',
			'name',
			'price',
			'cat',
			'prov',
			'stat',
			'img',
		]
		labels = {
			'barcode' : 'Codigo de barras',
			'name' : 'Nombre',
			'price' : 'Precio',
			'cat' : 'Categoria',
			'prov' : 'Proveedor',
			'stat' : 'Estado',
			'img' : 'Imagen',
		}

	def __init__(self, *args, **kwargs):
		super(productForm,self).__init__(*args,**kwargs)
		self.fields['barcode'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['name'].widget.attrs.update({'class':'mdl-textfield__input'})		
		self.fields['price'].widget.attrs.update({'class':'mdl-textfield__input'})	
		self.fields['cat'].widget.attrs.update({'class':'mdl-cell mdl-cell--12-col'})
		self.fields['prov'].widget.attrs.update({'class':'mdl-cell mdl-cell--12-col'})
		self.fields['stat'].widget.attrs.update({'class':'mdl-cell mdl-cell--12-col'})
		self.fields['prov'].queryset = Proveedor.objects.exclude(estado = '2')

