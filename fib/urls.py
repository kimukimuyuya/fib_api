from django.urls import path
from . import views

urlpatterns = [
  path('fib', views.fib_api, name='fib_api')
]