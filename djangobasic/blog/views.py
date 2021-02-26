from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def hello(request):
    # return HttpResponse("<h2>HelloWorld</h2>")
    tags = ["น้ำตก","ธรรมชาติ",'หน้าฝน']
    rating = 4
    return render(request,"index.html",
    {
        'name' : 'บทความท่องเที่ยวภาคเหนือ',
        'author' : "noppagorn",
        'tags' : tags,
        'rating' : rating
    })

def page1(request):
    return render(request,'page1.html')