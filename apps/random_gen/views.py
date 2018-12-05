from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string




# Create your views here.
def index(request):
    return render(request, 'random_gen/index.html')

def randomeword(number):
    return (get_random_string(length=number))

def generate(request):
    if "count" not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    request.session['randomness'] = randomeword(14)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
