from django.shortcuts import render, redirect, render_to_response
from django.shortcuts import HttpResponse, HttpResponseRedirect
from hashlib import sha1
from django.http import JsonResponse
from .models import *
from django import forms


# Create your views here.

# class UserForm(forms.Form):
#     Username = forms.CharField(label='用户名', max_length=50)
#     password = forms.CharField(label='密码', widget=forms.PasswordInput())
#     email = forms.EmailField(label='邮箱')

#注册界面展示
def register(request):
    return render(request, 'userapphtml/register.html')

#注册信息保存
def registsave(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    if upwd != upwd2:
        return redirect('/userapp/register')

    sl = sha1()
    sl.update(upwd.encode('utf8'))
    upwd3 = sl.hexdigest()

    # print(uname, upwd3)
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect('/userapp/login')

def userexist(request):
    uname = request.GET.get('uname', '')
    print(uname)
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count1': count})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('pwd', '')
        s1 = sha1()
        s1.update(password.encode('utf8'))
        user = UserInfo.objects.filter(uname=username, upwd=s1.hexdigest())
        if user:
            response = HttpResponseRedirect('/sucapp/main')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return render(request, 'userapphtml/login.html', {'error':'用户名或密码错误！'})
            # return HttpResponse('用户名或密码错误！')
    else:
        return render(request, 'userapphtml/login.html')

def logout(request):
    response = HttpResponseRedirect('/sucapp/main')
    response.delete_cookie('username')
    return response





# def register(request):
#     if request.method == 'POST':
#         Userform = UserForm(request.POST)
#         if Userform.is_valid():
#             Username = Userform.cleaned_data['Username']
#             password = Userform.cleaned_data['password']
#             email = Userform.cleaned_data['email']
#
#             UserInfo.objects.create(Username=Username, password=password, email=email)
#             UserInfo.save()
#
#             return HttpResponse('regist success!!!')
#     else:
#         Userform = UserForm()
#     return render_to_response('userapphtml/register.html', {'Userform': Userform})
#
#
# def login(request):
#     if request.method == 'POST':
#         Userform = UserForm(request.POST)
#         if Userform.is_valid():
#             Username = Userform.cleaned_data['Username']
#             password = Userform.cleaned_data['password']
#
#             User = UserInfo.objects.filter(Username__exact=Username, password__exact=password)
#
#             if User:
#                 return render_to_response('sucapphtml/index.html', {'Userform': Userform})
#             else:
#                 return HttpResponse('用户名或密码错误,请重新登录')
#
#     else:
#         Userform = UserForm()
#     return render_to_response('userapphtml/login.html', {'Userform': Userform})
