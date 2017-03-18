from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
	TYPE_CHOICES = (
		('1', 'Male'),
		('0', 'Felmale'),
		)
	user = models.ForeignKey(User, null=True)
	gender = models.CharField(max_length=1, choices=TYPE_CHOICES, default=1)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False)
	date = models.DateTimeField(default=datetime.now())
	avtar = models.ImageField(upload_to = '/avatar', default = '/avatar/no-img.jpg', null=True)

class Blog(models.Model):
	user = models.ForeignKey(User, null=True)
	title = models.CharField(max_length=200, null=True)
	content = models.TextField(null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False)
	image = models.ImageField(upload_to = '', default = 'no-img.jpg')
	rate = models.IntegerField(default =0)