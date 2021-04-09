from django.shortcuts import render
from django.views.generic import TemplateView

# main page view
def homeview(request):
    return render(request,'home.html',{})
# research papers section view
class papers(TemplateView):
        template_name = "papers.html"