from django.urls import path
from . import views

urlpatterns = [
   path('payments/v2/create', views.payment_create_view, name='payment_create'),
]