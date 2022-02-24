from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate, decorators
from django.urls import reverse
# Create your views here.
def Login(request):
    if request.POST:
        username= request.POST.get('Username')
        password= request.POST.get('Password')
        my_user = authenticate(username=username, password=password)
        if my_user is None:
            return render(request,'login.html',{'loi':'Tài Khoản hoặc mật khẩu không chính xác vui lòng nhập lại'})
        login(request,my_user)
        return HttpResponseRedirect(reverse('home',))

    else:
        return render(request,'login.html')
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home',))
