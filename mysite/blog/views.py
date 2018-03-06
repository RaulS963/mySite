from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
     return render(request, 'mainpage.html')

def personal(request):
     return render(request, 'personal.html')

def about(request):
     return render(request, 'about.html')	 