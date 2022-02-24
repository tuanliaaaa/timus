from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Product,Buy,Users
from django.urls import reverse
from django.contrib.auth import authenticate,decorators
def index(request):
    list_watch = Product.objects.all()[0:8]
    for i in list_watch:
        a = i.img.split(',')
        i.imgs = a
    return render(request,'home/index.html',{'list_watch':list_watch})
def watches(request):
    if request.GET:
        search = request.GET['search']
        list_watch = Product.objects.filter(ProductCode__contains=search)|Product.objects.filter(ProductName__contains=search)
        for i in list_watch:
            a = i.img.split(',')
            i.imgs = a
        return render(request,'home/watches.html',{'list_watch':list_watch})
    else:
        list_watch = Product.objects.all()[0:8]
        for i in list_watch:
            a = i.img.split(',')
            i.imgs = a
        return render(request,'home/watches.html',{'list_watch':list_watch})
def card(request):
    List_Buy = Buy.objects.order_by("-BuyTime").all()[0:5]
    for i in List_Buy:
        a = i.Product.img.split(',')
        i.Product.imgs = a
    return render(request,'home/card.html',{'List_Buy':List_Buy})
def singerProduct(request,id):
    ok=True
    try:
        list_singerProduct = Product.objects.get(pk=id)
    except:
        return render(request,'home/singerProduct.html',{'unpip':'Sản Phẩm không tồn tại chuyển đến trang chủ trong giây lát.'})
    a = list_singerProduct.img.split(',')
    if request.POST:    
        quantily = request.POST['quantily']
        UserName = request.POST['UserName']
        Sex = request.POST['Sex']
        Number = request.POST['Number']
        email = request.POST['email']
        c = Users.objects.all()
        dem=0
        for i in c:
            if email == i.email or Number == i.Number:
                dem+=1
                g=i.id
                break
        if dem==0:  
            d = Users(UserName=UserName,Sex=Sex,Number=Number,email=email)
            d.save()
        else:
            d=Users.objects.get(pk=g)
        b = Buy(Product=list_singerProduct,quantily=quantily,Users=d)
        b.save()
        list_singerProduct.stock-=int(quantily)
        list_singerProduct.save()
        return HttpResponseRedirect(reverse('card',))
    return render(request,'home/singerProduct.html',{'singerProduct':list_singerProduct,'ims':a,'ok':ok})
def showAll(request):
    
    list_watch = Product.objects.all()
    for i in list_watch:
        a = i.img.split(',')
        i.imgs = a
    return render(request,'home/watches.html',{'list_watch':list_watch})
def DeleteProduct(request,id):
    list_singerProduct = Product.objects.get(pk=id)
    list_singerProduct.delete()
    return HttpResponseRedirect(reverse('singerProduct',args=(id,)))
@decorators.login_required(login_url='login')
def EditProduct(request,id):
    list_singerProduct = Product.objects.get(pk=id)
    if request.POST:
        ProductName =request.POST['ProductName']
        ProductCode = request.POST['ProductCode']
        price = request.POST['price']
        stock = request.POST['stock']
        describe = request.POST['describe']
        img = request.POST['img']
        list_singerProduct.ProductName=ProductName
        list_singerProduct.ProductCode=ProductCode
        list_singerProduct.price = price
        list_singerProduct.stock = stock
        list_singerProduct.describe =describe
        list_singerProduct.img = img
        list_singerProduct.save()
        return HttpResponseRedirect(reverse('singerProduct',args=(id,)))
    return render(request,'EditProduct.html',{'list_singerProduct':list_singerProduct})
@decorators.login_required(login_url='login')
def AddProduct(request):
    if request.POST:
        ProductName =request.POST['ProductName']
        ProductCode = request.POST['ProductCode']
        price = request.POST['price']
        stock = request.POST['stock']
        describe = request.POST['describe']
        img = request.POST['img']
        a = Product(ProductName=ProductName,ProductCode=ProductCode,price=price,stock=stock,describe=describe,img=img)
        a.save()
        return HttpResponseRedirect(reverse('singerProduct',args=(a.id,)))
    return render(request,'home/AddProduct.html')