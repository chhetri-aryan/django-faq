from django.urls import path
from . import views

urlpatterns = [
    path('faqs/', views.get_faqs),
]
