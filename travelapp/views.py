from django.shortcuts import render
from django.http import HttpResponse 
from .models import place,team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    tm=team.objects.all()
    return render(request,'index.html',{'result':obj,'team':tm})