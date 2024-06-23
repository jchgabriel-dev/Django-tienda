from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth import login, logout, authenticate
from .form import clientRegister, adminRegister, UpdateUser, AdmUpdate, CliUpdate,LoginForm, PasswordChangeForm
from .models import Client, Adm, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here. 

class registerClient(CreateView):
	model = User
	form_class = clientRegister
	template_name = 'cuentas/registerClient.html'
	
	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'Client'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('/')

class registerAdmin(CreateView):
	model = User
	form_class = adminRegister
	template_name = 'cuentas/registerAdmin.html'
	
	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'Adm'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('/')


def loginUser(request):
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.error(request, "Contraseña o usuario incorrectos")

		else:
			messages.error(request, "Contraseña o usuario incorrectos")
	else:
		form = LoginForm(use_required_attribute=False)		

	context = {'form': form}
	return render(request, 'cuentas/login.html', context)
	

def logoutUser(request):
	logout(request)
	return redirect('/') 

class listAdmin(ListView):
	model = Adm
	template_name = 'cuentas/listAdmin.html'
	queryset = Adm.objects.all()

def profileadm(request):
	if request.method == 'POST':
		u_form = UpdateUser(request.POST, instance=request.user)
		a_form = AdmUpdate(request.POST, request.FILES, instance=request.user.adm)
		if u_form.is_valid() and a_form.is_valid:
			u_form.save()
			a_form.save()
			return redirect('profileadm')
	else: 
		u_form = UpdateUser(instance=request.user)
		a_form = AdmUpdate(instance=request.user.adm)

	context = {
	'u_form' : u_form,
	'a_form' : a_form,
	}
	return render(request, 'cuentas/profileA.html', context)

def profilecli(request):
	if request.method == 'POST':
		u_form = UpdateUser(request.POST, instance=request.user)
		a_form = CliUpdate(request.POST, request.FILES, instance=request.user.adm)
		if u_form.is_valid() and a_form.is_valid:
			u_form.save()
			a_form.save()
			return redirect('profileadm')
	else: 
		u_form = UpdateUser(instance=request.user)
		a_form = CliUpdate(instance=request.user.client)

	context = {
	'u_form' : u_form,
	'a_form' : a_form,
	}
	return render(request, 'cuentas/profileC.html', context)


def password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('profileadm')

		else:
			return redirect('profileadm')
	else: 
		form = PasswordChangeForm(user=request.user)

	context = {
	'form' : form,
	}
	return render(request, 'cuentas/password.html', context)

