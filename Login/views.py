from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import User,Store


# Create your views here.
def index(request):
    template = loader.get_template('login/home.html')
    context={'title':'Savegenie','id':'1'}
    return HttpResponse(template.render(context,request))
def login(request,user_id):
    template = loader.get_template('login/index.html')
    context = {"title": "store",}
    return HttpResponse(template.render(context, request))

def store(request):
    template = loader.get_template('login/StorePage.html')
    email="avc"
    password="123"
    try:
     user = User()
     user.title = request.POST['head']
     user.first_name = request.POST['firstname']
     user.last_name = request.POST['lastname']
     user.email = request.POST['email']
     user.password = request.POST['pass']
     password = request.POST['pass']
     email=user.email;
     user.repassword = request.POST['repass']
     user.mobile = request.POST['mobile']
     user.save()
    except Exception,arg:
        print "error"


    list=Store.objects.all()
    context = {"title": "login" ,"list": list,'valid':"validuser",'password':"rightpass"}
    return HttpResponse(template.render(context, request))
def userlogin(request):
    template = loader.get_template('login/StorePage.html')
    email = request.POST['email']
    password =  request.POST['pass']
    #validuser=User.objects.filter(email=email)
    rightpass=0
    validuser=get_object_or_404(User,email=email)
    if(password==validuser.password):
            print "rightpassword"
            rightpass=1
    else:
        print "wrongpassword"
        rightpass=0


    list=Store.objects.all()
    context = {"title": "login" ,"list": list,'valid':validuser,'password':rightpass}
    return HttpResponse(template.render(context, request))