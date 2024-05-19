from django.urls import path
from .views import productspageview
from .views import profilepageview

urlpatterns = [
    path("product", productspageview, name="products"),
    path("profile", profilepageview, name="profile")
]