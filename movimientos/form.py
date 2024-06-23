from django import forms
from .models import Movimiento
from django.shortcuts import get_object_or_404

class MovForm(forms.ModelForm):
	class Meta:
		model = Movimiento
		fields = [
			'entry',
			'quant',
		]
		labels = {
			'entry' : 'movimiento',
			'quant' : 'cantidad',
		}

	def __init__(self, *args, **kwargs):
		super(MovForm,self).__init__(*args,**kwargs)
		self.fields['entry'].widget.attrs.update({'class':'mdl-checkbox__input'})					
		self.fields['quant'].widget.attrs.update({'class':'mdl-textfield__input'})

