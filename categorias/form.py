from django import forms
from .models import Categoria

class categoryForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = [
			'name',
			'desc',
		]
		labels = {
			'name' : 'Nombre',
			'desc' : 'Descripcion',
		}

	def __init__(self, *args, **kwargs):
		super(categoryForm,self).__init__(*args,**kwargs)
		self.fields['name'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['desc'].widget.attrs.update({'class':'mdl-textfield__input'})	