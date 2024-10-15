from django.shortcuts import render

# Create your views here.
from .models import userdetailes
def userdata(request):
    if request.method=="GET":
        k=userdetailes.objects.order_by('firstname')
        return render (request,"u.html",{'k':k})
def userdata1(request):
    if request.method=="GET":
        k=userdetailes.objects.order_by('-firstname')
        return render (request,"u.html",{'k':k})
def userdata2(request):

    if request.method=="POST":
        st=request.POST.get('fname')
        k=userdetailes.objects.filter(firstname__icontains=st)
        return render (request,"u.html",{'k':k})
    else:
        k=userdetailes.objects.all()
        return render (request,"u.html",{'k':k})
