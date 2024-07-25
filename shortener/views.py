import string
import random
from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from .models import URL

BASE62 = string.ascii_letters + string.digits

def generate_short_code(length=7):
    return ''.join(random.choices(BASE62, k=length))

def homepage(request):
    return render(request, 'homepage.html')

def index(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_code = generate_short_code()
        while URL.objects.filter(short_url=short_code).exists():
            short_code = generate_short_code()
        short_url = f"{request.build_absolute_uri('/')}{short_code}"
        URL.objects.create(long_url=long_url, short_url=short_code)
        return render(request, 'shortener/url_output.html', {'short_url': short_url})
    return render(request, 'shortener/index.html')

def redirect_url(request, short_code):
    url = URL.objects.filter(short_url=short_code).first()
    if url:
        return redirect(url.long_url)
    return HttpResponse('URL not found', status=404)