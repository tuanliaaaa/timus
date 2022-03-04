from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Product,Buy,Users
from django.urls import reverse
from django.contrib.auth import authenticate,decorators
from django.core.mail import send_mail
from django.db.models import Count,Sum
import datetime
def index(request):
    list_watch = Product.objects.all()[0:8]
    for i in list_watch:
        a = i.img.split(',')
        i.imgs = a
        i.price = int((100-i.sale)*i.price/100)
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
            i.price = int((100-i.sale)*i.price/100)
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
    if list_singerProduct.sale !=0 :
        list_singerProduct.vcl = int((100-list_singerProduct.sale)*list_singerProduct.price/100)
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
        i.price = int((100-i.sale)*i.price/100)
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
        sale = request.POST['Sale']
        list_singerProduct.ProductName=ProductName
        list_singerProduct.ProductCode=ProductCode
        list_singerProduct.price = price
        list_singerProduct.stock = stock
        list_singerProduct.describe =describe
        list_singerProduct.img = img
        list_singerProduct.sale = sale
        list_singerProduct.save()
        if list_singerProduct.sale != 0:
            list_user = Users.objects.all()
            h=[]
            for i in list_user:
                h.append(i.email)
            print(h)
            content_mail= 'Hiện nay bên shop chúng em đang sale sản phẩm: ' + list_singerProduct.ProductName + ' '+ list_singerProduct.sale + '% \n'+ 'http://127.0.0.1:8000/singerProduct/5/'
            send_mail('Subject here',content_mail, 'buitrung446646@gmail.com', ['nhattuan44t@gmail.com'], fail_silently=False)
        return HttpResponseRedirect(reverse('singerProduct',args=(id,)))
    return render(request,'EditProduct.html',{'list_singerProduct':list_singerProduct})
@decorators.login_required(login_url='login')
def AddProduct(request):
    loi=False
    if request.POST:
        ProductName =request.POST['ProductName']
        ProductCode = request.POST['ProductCode']
        price = request.POST['price']
        stock = request.POST['stock']
        describe = request.POST['describe']
        img = request.POST['img']
        b=Product.objects.all()
        for i in b:
            if ProductCode == i.ProductCode:
                dem=1
                break
        if dem==1:
            loi=True
            return render(request,'home/AddProduct.html',{'loi':loi,'ProductName':ProductName,'price':price,'stock':stock,'describe':describe,'img':img})
        a = Product(ProductName=ProductName,ProductCode=ProductCode,price=price,stock=stock,describe=describe,img=img)
        a.save()
        return HttpResponseRedirect(reverse('singerProduct',args=(a.id,)))
    return render(request,'home/AddProduct.html')
@decorators.login_required(login_url='login')
def manager(request):
    if request.GET:
        h= request.GET['DayStart']
        k=request.GET['DayEnd']
        p=h.split('/')
        q=k.split('/')
        dt1 = datetime.datetime(int(p[2]), int(p[1]), int(p[0]), 0, 0, 0,0)
        dt2 = datetime.datetime(int(q[2]), int(q[1]), int(q[0]), 0, 0, 0,0)
        dt2 = dt2 + datetime.timedelta(days=1)
        b=int(request.GET['ChooseMode'])
        a = Buy.objects.filter(BuyTime__gt=dt1,BuyTime__lt=dt2)
        if b==1:
            tongdoanhthu=0
            for i in a:
                tongdoanhthu+=i.quantily*i.Product.price
            return render(request,'home/card.html',{'b':b,'tongdoanhthu':tongdoanhthu,'DayStart':h,'DayEnd':k})
        elif b==2:
            ListUser = Users.objects.filter(buy__BuyTime__gt=dt1,buy__BuyTime__lt=dt2).annotate(Count('buy__quantily')).order_by('-buy__quantily__count')[0:5]
            return render(request,'home/card.html',{'b':b,'ListUser':ListUser,'DayStart':h,'DayEnd':k})
        elif b==3:
            ListProduct = Product.objects.filter(buy__BuyTime__gt=dt1,buy__BuyTime__lt=dt2).annotate(Sum('buy__quantily')).order_by('-buy__quantily__sum')[0:5]
            for i in ListProduct:
                a = i.img.split(',')
                i.imgs = a
                i.TotalMoney = i.price * i.buy__quantily__sum
            return render(request,'home/card.html',{'b':b,'ListProduct':ListProduct,'DayStart':h,'DayEnd':k})
        elif b==4:
            List_Buy = Buy.objects.filter(BuyTime__gt=dt1,BuyTime__lt=dt2).order_by("-BuyTime").all()[0:5]
            for i in List_Buy:
                a = i.Product.img.split(',')
                i.Product.imgs = a
                i.TotalMoney = i.quantily * i.Product.price
            return render(request,'home/card.html',{'b':b,'List_Buy':List_Buy,'DayStart':h,'DayEnd':k})
    List_Buy = Buy.objects.order_by("-BuyTime").all()[0:5]
    for i in List_Buy:
        a = i.Product.img.split(',')
        i.Product.imgs = a
        i.TotalMoney = i.quantily * i.Product.price
    return render(request,'home/card.html',{'List_Buy':List_Buy})
  