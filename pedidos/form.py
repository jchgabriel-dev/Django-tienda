from django import forms
from .models import Pedido

class PedForm(forms.ModelForm):
	class Meta:
		model = Pedido
		fields = [
			'quantity',
		]
		labels = {
			'quantity' : 'cantidad',
		}

	def __init__(self, *args, **kwargs):
		super(PedForm,self).__init__(*args,**kwargs)
		self.fields['quantity'].widget.attrs.update({'class':'mdl-textfield__input'})

