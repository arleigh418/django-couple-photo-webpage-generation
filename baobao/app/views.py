"""
Definition of views.
"""

from datetime import datetime
from email.message import EmailMessage
from pickle import FALSE
from tkinter.tix import ROW, Form
from urllib.request import Request
from django.shortcuts import redirect,render
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .forms import RegisterForm,LoginForm,HomeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
from .sweet_bao import generate_sweet_bao_template
import os

    


def home(request):
    if request.user.is_authenticated:
        sweet_bao_url = os.path.dirname(__file__)+r"\\templates\\sweet_bao\\"
        sweet_bao_domain = '/sweet_bao/'

        #獲取驗證碼
        user_select = f"'{request.user}'"
        active_list, end_date_list = [],[]
        if_active = 'N'
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT active_number,end_date FROM baobao.active_number where account = {user_select}")
            row = cursor.fetchone()
            if row:
                active_list.append(row[0])
                end_date_list.append(row[1].strftime('%Y/%m/%d'))   
            if len(active_list)>0:if_active='Y'
        cus_active_info = zip(active_list,end_date_list)

        #傳送表單時
        if request.method == "POST":
            form = HomeForm(request.POST, request.
                            FILES)
            if form.is_valid():
                #獲取當前user且篩選出它的資訊
                current_user = auth.get_user(request)
                user_info_get = love_bao.objects.filter(username=current_user).first()
                user_info = model_to_dict(user_info_get)

                #如果user資訊不是空的,為既有客戶,刪除他的html file
                if user_info_get is not None:
                    user_info = model_to_dict(user_info_get)
                    past_url = user_info['url_def']+'.html'
                    cust_url = sweet_bao_domain +str(user_info['url_def'])+'.html'
                    if (os.path.exists(f'{sweet_bao_url}{past_url}')):
                        os.remove(f'{sweet_bao_url}{past_url}')
                else:
                    cust_url=''

                save_info = form.save(commit=False)
                #如果前面有圖片的話,繼續保存,避免客戶一直傳
                if not save_info.banner_pic:
                    if user_info_get.banner_pic:
                        save_info.banner_pic = user_info_get.banner_pic
                if not save_info.left_bao_pic:
                    if user_info_get.left_bao_pic:
                        save_info.left_bao_pic = user_info_get.left_bao_pic
                if not save_info.right_bao_pic:
                    if user_info_get.right_bao_pic:
                        save_info.right_bao_pic = user_info_get.right_bao_pic
                if not save_info.bao_six_pic1:
                    if user_info_get.bao_six_pic1:
                        save_info.bao_six_pic1 = user_info_get.bao_six_pic1
                if not save_info.bao_six_pic2:
                    if user_info_get.bao_six_pic2:
                        save_info.bao_six_pic2 = user_info_get.bao_six_pic2
                if not save_info.bao_six_pic3:
                    if user_info_get.bao_six_pic3:
                        save_info.bao_six_pic3 = user_info_get.bao_six_pic3
                if not save_info.bao_six_pic4:
                    if user_info_get.bao_six_pic4:
                        save_info.bao_six_pic4 = user_info_get.bao_six_pic4
                if not save_info.bao_six_pic5:
                    if user_info_get.bao_six_pic5:
                        save_info.bao_six_pic5 = user_info_get.bao_six_pic5
                if not save_info.bao_six_pic6:
                    if user_info_get.bao_six_pic6:
                        save_info.bao_six_pic6 = user_info_get.bao_six_pic6
                
                save_info.username = current_user
                love_bao.objects.filter(username=current_user).delete()    
                save_info.save()
                user_info_get = love_bao.objects.filter(username=current_user).first()
                user_info = model_to_dict(user_info_get)
                html_get = generate_sweet_bao_template(user_info)
                
                with open(f"{sweet_bao_url}{user_info['url_def']}.html", "a",encoding='utf-8') as file:
                    file.write(html_get)
                messages.error(request,'填寫成功!! 快去看看你們的專屬頁面')
             
            else:
                messages.error(request,'表單填寫有誤,可能是自訂寶寶的專屬網址重複')
                return render(request, 'app/index.html', locals())
               
        else:
            current_user = auth.get_user(request)
            user_info_get = love_bao.objects.filter(username=current_user).first()
            if user_info_get is not None:
                user_info = model_to_dict(user_info_get)
                cust_url = sweet_bao_domain +str(user_info['url_def'])+'.html'
                user_info['bao_together_date'] = user_info['bao_together_date'].strftime('%Y-%m-%d')
                if user_info['bao_big_thing_date1']:
                    user_info['bao_big_thing_date1'] = user_info['bao_big_thing_date1'].strftime('%Y-%m-%d')
                if user_info['bao_big_thing_date2']:
                    user_info['bao_big_thing_date2'] = user_info['bao_big_thing_date2'].strftime('%Y-%m-%d')
                if user_info['bao_big_thing_date3']:
                    user_info['bao_big_thing_date3'] = user_info['bao_big_thing_date3'].strftime('%Y-%m-%d')
                if user_info['bao_big_thing_date4']:
                    user_info['bao_big_thing_date4'] = user_info['bao_big_thing_date4'].strftime('%Y-%m-%d')
                
            else:
                user_info={}
                cust_url=''
            
            form = HomeForm(initial=user_info)
        return render(request, 'app/index.html', {'form':form,'active_info':cus_active_info,'cust_url':cust_url,'if_active':if_active})
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

def handler404(request,exception,template_name='404.html'):
    response = render(template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    return render(request, 'app/500.html', status=500)

