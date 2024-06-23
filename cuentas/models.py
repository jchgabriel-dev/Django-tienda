from django.db import models
from django.contrib.auth.models import AbstractUser
from productos.models import Producto
# Create your models here

class User(AbstractUser):
	is_admin = models.BooleanField(default=False)
	is_client = models.BooleanField(default=False)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	photo = models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Client'


class Adm(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	photo = models.ImageField(default='default.jpg',upload_to='profile_pics')	

	def __str__(self):
		return f'{self.user.username} Adm'