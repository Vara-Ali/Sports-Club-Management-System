from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def gadgets(request):
    return render(request, 'dashboard/Gadgets.html')