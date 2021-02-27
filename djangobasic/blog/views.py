from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
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

def addBlog(request):
    # change to post because GET show data in url
    name = request.POST['name']
    description = request.POST["description"]
    return render(request,'result.html',{
        'name' : name,
        'description' : description,
    })