from django.shortcuts import render

def index(request):
    return render(request, 'TurtleMasterApp/index.html')
# Create your views here.
