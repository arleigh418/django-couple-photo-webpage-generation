"""
Definition of views.
"""

from datetime import datetime
from email.message import EmailMessage
from pickle import FALSE
from tkinter.tix import ROW, Form
from urllib.request import Request
from django.shortcuts import redirect,render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .forms import RegisterForm,LoginForm,HomeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings
from django.db import connection
from django.contrib import auth
from .models import love_bao
from django.forms.models import model_to_dict

def home(request):
    if request.user.is_authenticated:
        user_select = f"'{request.user}'"
        active_list, end_date_list = [],[]
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT active_number,end_date FROM baobao.active_number where account = {user_select}")
            row = cursor.fetchone()
            if row:
                active_list.append(row[0])
                end_date_list.append(row[1].strftime('%Y/%m/%d'))   
        cus_active_info = zip(active_list,end_date_list)
        if request.method == "POST":
            form = HomeForm(request.POST, request.
                            FILES)
            if form.is_valid():
                current_user = auth.get_user(request)
                save_info = form.save(commit=False)
                save_info.username = current_user
                save_info.save()
        else:
            current_user = auth.get_user(request)
            user_info_get = love_bao.objects.filter(username=current_user).first()
            if user_info_get is not None:
                user_info = model_to_dict(user_info_get)
            else:
                user_info={}
            form = HomeForm(initial=user_info)
        return render(request, 'app/index.html', {'form':form,'active_info':cus_active_info})
    else:
        return render(request,'app/index.html')
        
    


def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'app/register.html', context)


def sign_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    if request.method =='POST':
        form = LoginForm()
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('/home')
        else:
            messages.error(request,'帳號或密碼錯誤')
            return render(request, 'app/login.html', locals())
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('/home') #重新導向到登入畫面



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))

			if associated_users.exists():
				for user in associated_users:
					title = "世界寶寶 - 密碼重置"
					email_template_name = "app/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(
                            title,
                            email,
                            settings.EMAIL_HOST_USER,
                            [user.email],
                            fail_silently=False
                            )
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="app/password_reset.html", context={"password_reset_form":password_reset_form})
