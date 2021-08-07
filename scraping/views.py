from django.shortcuts import render
from django.contrib import messages

# Main index
def index(request):
    return render (request, 'index.html')