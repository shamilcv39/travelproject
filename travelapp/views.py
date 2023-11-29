from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Place, Team1


# Create your views here.


def demo(request):
    obj = Place.objects.all()
    abj=Team1.objects.all()
    # name="india"
    return render(request, "index.html", {'result': obj,"data":abj})

    # {'obj':name})




# def about(request):
# return render(request,"about.html")

# def contact(request):
# return HttpResponse("hello am contact")

# def addition(request):
# x=int(request.GET['num1'])
# y=int(request.GET['num2'])
# res=x+y
# return render(request,"result.html",{'result':res})
