from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reserve/<int:spot_id>/', views.reserve_parking, name='reserve_parking'),
]
