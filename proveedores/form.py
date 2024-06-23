from django import forms
from .models import Proveedor

class providerForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = [
			'persona',
			'direccion',
			'email',
			'telefono',
			'estado',
		]
		labels = {
			'persona' : 'Persona de Contacto',
			'direccion' : 'Direccion',
			'email' : 'email',
			'telefono' : 'celular',
			'estado' : 'Estado'
		}

	def __init__(self, *args, **kwargs):
		super(providerForm,self).__init__(*args,**kwargs)
		self.fields['persona'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['direccion'].widget.attrs.update({'class':'mdl-textfield__input'})	
		self.fields['email'].widget.attrs.update({'class':'mdl-textfield__input'})	
		self.fields['telefono'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['estado'].widget.attrs.update({'class':'mdl-checkbox__input'})					
