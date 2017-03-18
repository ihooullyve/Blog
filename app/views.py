from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile, Blog
from django.http import HttpResponse, JsonResponse
import json
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	return render(request, 'app/templates/index.html')

def test(request):
	return render(request, 'app/templates/test.html')

def signup(request):
	username = request.GET.get('username')
	email = request.GET.get('email')
	gender = request.GET.get('gender')
	date = request.GET.get('date')
	password = request.GET.get('password')
	re_password = request.GET.get('re_password')

	obj = User(username = username, email=email, password = password)
	obj.set_password(password)
	obj.save()
	obj_profile = Profile(user = obj, gender = gender)
	obj_profile.save()

	response = {
		'result' : 1,
	}

	return JsonResponse(response)

@csrf_exempt
def login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	try:
		obj_user = User.objects.get(username = username)
		if obj_user.check_password(password):
			response = {
				'result' : 1,
			}
		else:
			response = {
				'result' : 0,
			}
	except:
		response = {
			'result' : -999,
		}
	return JsonResponse(response)

@csrf_exempt
def add_blog(request):
	user = request.POST.get('user')
	title = request.POST.get('title')
	content = request.POST.get('text')

	obj_user = User.objects.get(id = user)
	obj_blog = Blog(user = obj_user, title=title, content=content)
	obj_blog.save()

	response = {
		'result' : 1,
	}
	return JsonResponse(response)

def list_all_blog(request):
	pageNumber = request.GET.get('page')
	totalCurrent = request.GET.get('total')
	print(pageNumber)
	obj_blog = Blog.objects.all().order_by('-updated')
	paginator = Paginator(obj_blog, totalCurrent)

	try:
		list_page = paginator.page(pageNumber)
	except PageNotAnInteger:
	    list_page = paginator.page(1)
	except EmptyPage:
	    list_page = paginator.page(paginator.num_pages)

	print(list(list_page))

	all_blog = []
	username = "null"
	for i in list(list_page):
		if i.user is not None:
			username = i.user.username
		else:
			username = "No Name"
		all_blog.append({
			'id' : i.id,
			'title' : i.title,
			'user' : username,
			'content' : i.content,
			'updated' : i.updated,
			'image_url' : i.image.url,
			'image_name' : i.image.name,
		})
	response = {
		'result' : 1,
		'data' : all_blog,
		'totalItems' : obj_blog.count(),
	}

	return JsonResponse(response)

def detail_blog(request):
	id = request.GET.get('id')

	obj = Blog.objects.get(id = id)
	username = ""
	if obj.user is not None:
		username = obj.user.username
	else:
		username = "No Name"
	response = {
		'result' : 1,
		'data' : {
			'id' : obj.id,
			'user' : username,
			'title' : obj.title,
			'content'	: obj.content,
			'updated' : obj.updated,
			'image_url' : obj.image.url,
			'image_name' : obj.image.name,
		}
	}

	return JsonResponse(response)

@csrf_exempt
def edit_blog(request):
	id = request.POST.get('id')
	title = request.POST.get('title')
	content = request.POST.get('content')

	for i in request.FILES.getlist('file'):
		obj = Blog.objects.get(id = id)
		obj.title = title
		obj.content = content
		obj.updated = timezone.now()
		obj.image = i
		obj.save()
		username = ""
		if obj.user is not None:
			username = obj.user.username
		else:
			username = "No Name"
		response = {
			'result' : 1,
			'data' : {
				'id' : obj.id,
				'title' : obj.title,
				'content' : obj.content,
				'updated' : obj.updated,
				'user' : username,
				'image_name' : obj.image.name,
			}
		}
	return JsonResponse(response)

@csrf_exempt
def upload_image(request):
	for i in request.FILES.getlist('file'):
		obj = Blog(image=i)
		obj.save()
		response = {
			'result' : obj.id,
		}
	return JsonResponse(response)

@csrf_exempt
def add_blog(request):
	title = request.POST.get('title')
	content = request.POST.get('content')
	for i in request.FILES.getlist('file'):
		obj = Blog(title = title, content = content, image = i)
		obj.save()

	response = {
		'result' : obj.id
	}
	return JsonResponse(response)

@csrf_exempt
def delete_blog(request):
	id = request.POST.get('id')

	obj = Blog.objects.get(id = id)
	obj.delete()

	response = {
		'result' : 1,
	}

	return JsonResponse(response)

def search(request):
	search = request.GET.get('search')
	obj = Blog.objects.filter(title__icontains = search).order_by('-updated')
	list_data = []
	for i in obj:
		username = ""
		if i.user is not None:
			username = i.user.username
		else:
			username = "No Name"
		list_data.append({
				'id' : i.id,
				'title' : i.title,
				'user' : username,
				'content' : i.content,
				'updated' : i.updated,
				'image_url' : i.image.url,
				'image_name' : i.image.name,
			})
	response = {
		'result': 1,
		'data' : list_data,
	}

	return JsonResponse(response)
