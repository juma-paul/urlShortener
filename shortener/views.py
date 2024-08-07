import string
import random
from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from .models import URL


def homepage(request):
    return render(request, 'homepage.html')

def base62_encode(number):
    """Encodes a number into a base62 string."""

    chars = string.ascii_letters + string.digits
    encoded = ''
    while number > 0:
        encoded = chars[number % 62] + encoded
        number //= 62

    return encoded

def generate_unique_short_code(length=7):
    """Generates a unique short code of the specified length."""

    while True:
        random_number = random.getrandbits(64)
        code = base62_encode(random_number)
        short_code = ''.join(random.choices(code, k=length))
        
        if not URL.objects.filter(short_url=short_code).exists():
            return short_code
        
def index(request):
    """Handle URL shortening and display the short URL."""

    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        
        url_entry = URL.objects.filter(long_url=long_url).first()
        
        if url_entry:
            short_code = url_entry.short_url
        else:
            short_code = generate_unique_short_code()
            
            while URL.objects.filter(short_url=short_code).exists():
                short_code = generate_unique_short_code()
            
            URL.objects.create(long_url=long_url, short_url=short_code)
        
        short_url = f"{request.build_absolute_uri('/')}short/{short_code}"
        context = {'short_url': short_url}
        
        return render(request, 'shortener/url_output.html', context)
    
    return render(request, 'shortener/index.html')

def redirect_url(request, short_code):
    """Redirect to the original URL based on the short code."""

    url = URL.objects.filter(short_url=short_code).first()
    if url:
        return redirect(url.long_url)
    
    return HttpResponse('URL not found', status=404)

def register(request):
    return render(request, "shortener/register.html")

def login(request):
    return render(request, "shortener/login.html")

def logout(request):
    return render(request, "homepage")