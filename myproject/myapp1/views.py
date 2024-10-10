from django.shortcuts import render

def luzon(request):
    return render(request, 'myapp1/luzon.html')

def visayas(request):
    return render(request, 'myapp1/visayas.html')

def mindanao(request):
    return render(request, 'myapp1/mindanao.html')
