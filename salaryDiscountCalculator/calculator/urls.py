from calculator import views
from django.urls import path

urlpatterns = [
    path('menu-principal/', views.main, name="main")
]
