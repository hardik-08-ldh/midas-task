from django.shortcuts import render
from django.views.generic import TemplateView

def homeview(request):
    return render(request,'home.html',{})
class papers(TemplateView):
        template_name = "papers.html"