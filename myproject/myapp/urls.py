from django.urls import path
from . import views

urlpatterns = [
    path('model/', views.model, name='model'),
    path('year/', views.year, name='year'),
    path('developer/', views.developer, name='developer'),
]
