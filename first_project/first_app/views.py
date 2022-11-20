from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Hello class, mubarak ho')
    my_greeting = {'insert_me':'Hello class'}
    return render(request, 'first_app/index.html', context=my_greeting)
