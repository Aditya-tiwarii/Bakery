from django.urls import path
from . import views

urlpatterns = [
    path('products-list/',views.ProductView.as_view()),
]
