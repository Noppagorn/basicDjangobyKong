from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Blog
from django.contrib.auth.models import User
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
            print("User name is existing")
            return redirect("/createForm")
        elif User.objects.filter(email=email).exists():
            print("Email is existing")
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
      return redirect("/createForm")
    # return render(request,'result.html')
    # return render()