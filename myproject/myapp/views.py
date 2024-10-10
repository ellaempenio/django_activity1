from django.shortcuts import render

def model(request):
    return render(request, 'myapp/model.html')

def year(request):
    return render(request, 'myapp/year.html')

def developer(request):
    return render(request, 'myapp/developer.html')
