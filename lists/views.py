from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')