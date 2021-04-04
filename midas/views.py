from django.shortcuts import render

def homeview(request):
    return render(request,'home.html',{'hello':'hi midas'})