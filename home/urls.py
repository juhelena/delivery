from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('produtos/<int:id>/', views.produtos, name='produtos'), 
]