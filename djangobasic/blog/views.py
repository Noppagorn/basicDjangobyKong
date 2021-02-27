from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Blog
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def hello(request):
    # return HttpResponse("<h2>HelloWorld</h2>")
    # tags = ["น้ำตก","ธรรมชาติ",'หน้าฝน']
    # rating = 4
    # return render(request,"index.html",
    # {
    #     'name' : 'บทความท่องเที่ยวภาคเหนือ',
    #     'author' : "noppagorn",
    #     'tags' : tags,
    #     'rating' : rating
    # })
    data = Blog.objects.all()
    return render(request,'index.html',{
        'blogs' : data
    })

def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request,'form.html')

def loginForm(request):
    return render(request,"login.html")
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    # login
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect("/")
    else:
        messages.info(request, "Not have this user")
        return redirect("/loginForm")
def logout(request):
    auth.logout(request)
    return redirect("/")
def addUser(request):
    # change to post because GET show data in url
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    # description = request.POST["description"]
    if password == repassword:
        if User.objects.filter(username=username).exists():
            # print("User name is existing")
            messages.info(request,"User name is existing")
            return redirect("/createForm")
        elif User.objects.filter(email=email).exists():
            print("Email is existing")
            messages.info(request, "Email is existing")
            return redirect("/createForm")
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname,
            )
            user.save()
            return redirect("/")
    else:
        messages.info(request,"Password not match")
        return redirect("/createForm")
    # return render(request,'result.html')
    # return render()