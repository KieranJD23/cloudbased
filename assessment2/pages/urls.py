from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductsPageView, ProductreviewsPageView, ReviewPageView, ProfilePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("products/", ProductsPageView.as_view(), name="products"),
    path("product-reviews/", ProductreviewsPageView.as_view(), name="product-reviews"),
    path("review/", ReviewPageView.as_view(), name="review"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
]