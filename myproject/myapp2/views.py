from django.shortcuts import render

def about(request):
    return render(request, 'myapp2/about.html')

def contact(request):
    return render(request, 'myapp2/contact.html')

def education(request):
    return render(request, 'myapp2/education.html')
