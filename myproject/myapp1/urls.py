from django.urls import path
from . import views

urlpatterns = [
    path('luzon/', views.luzon, name='luzon'),
    path('visayas/', views.visayas, name='visayas'),
    path('mindanao/', views.mindanao, name='mindanao'),
]
