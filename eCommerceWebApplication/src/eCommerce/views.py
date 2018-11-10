from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm





def home_page(request):
	context = {
		'title' : "Hello World!",
		'content' :"We are in Homepage."
	}
	return render(request,"home.html",context)

def about_page(request):
	context = {
		'title' : "about page!",
		'content' :"We are in About Page."	
	}
	return render(request,"about.html",context)

def contact_page(request):
	# contact_form = ContactForm(request.POST or None)
	contact_form = ContactForm()
	context = {
		"title" : "Contact us.",
		"content" : "Please fill up the Contact form.",
		"form" : contact_form
	}
	# if contact_form.is_valid():
	# 	print(contact_form.cleaned_data)
	if request.method == "POST":
		# print(request.POST)
		print(request.POST.get('fullname'))
		print(request.POST.get('email'))
		print(request.POST.get('content'))
	return render(request,"contact/view.html",context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		'title' : "Login!",
		'content' :"Please enter your username and password.",
		'form' : form	
	}
	print("User logged in")
	# print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username,password=password)
		print(user)
		# print(request.user.is_authenticated())
		if user is not None:
			login(request, user)
			# print(request.user.is_authenticated())
			# Redirect to a sucess message.
			# context['form'] = LoginForm()
			return redirect("/admin")
		else:
			print('Login Error!')

	return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
	register_form = RegisterForm(request.POST or None)
	context = {
		'title' : "Register new user",
		'content' :"This is register page",
		'form': register_form
	}
	if register_form.is_valid():
		print(register_form.cleaned_data)
		username = register_form.cleaned_data.get("username")
		email = register_form.cleaned_data.get("email")
		password = register_form.cleaned_data.get("password")
		new_user = User.objects.create_user(username,email,password)
		print(new_user)
	return render(request,"auth/register.html",context)

# def login_page(request):
# 	# login_form = LoginForm(request.POST or None)
# 	login_form = LoginForm()
# 	context = {
# 		'title' : "Login",
# 		'content' :"Enter your userename & password to login",	
# 		"form" : login_form
# 	}
# 	# if contact_form.is_valid():
# 	# 	print(contact_form.cleaned_data)
# 	if request.method == "POST":
# 		# print(request.POST)
# 		print(request.POST.get('username'))
# 		print(request.POST.get('password'))
# 	return render(request,"auth/login.html",context)

# def home_page_old(request):
# 	html_ = """
# 		<html lang="en">
# 	  <head>
# 	    <!-- Required meta tags -->
# 	    <meta charset="utf-8">
# 	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

# 	    <!-- Bootstrap CSS -->
# 	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">

# 	    <title>Hello, world!</title>
# 	  </head>
# 	  <body>
# 	  	<div class ='text-center'
# 	    	<h1>Hello, world!</h1>
# 	    </div>
# 	    <!-- Optional JavaScript -->
# 	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
# 	    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
# 	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
# 	    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
# 	  </body>
# 	</html>
# 	"""
# 	return HttpResponse(html_)