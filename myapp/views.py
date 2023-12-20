from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import Link
from django.http import HttpResponseRedirect

def scrape(request):
    if request.method =="POST":
        site = request.POST.get('site',"")
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')
    
        link_adress = []
        for link in soup.find_all('a'):
            link_adress = link.get('href')
            link_text = link.string
            Link.objects.create(adress=link_adress,name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
        
    return render(request,'myapp/result.html',{'data':data})


def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')

