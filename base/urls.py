from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductList.as_view()),
    path('products/<int:pk>', ProductDetails.as_view()),
]