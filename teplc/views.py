from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def index(request):
    return render(request, 'index.html')


def pay(request):
    return render(request, 'pay.html')


def delivery(request):
    return render(request, 'delivery.html')

def contact(request):
    return render(request, 'contact.html')