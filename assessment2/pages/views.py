from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"
class AboutPageView(TemplateView):
    template_name = "about.html"
class ContactPageView(TemplateView):
    template_name = "contact.html"
class ProductsPageView(TemplateView):
    template_name = "products.html"
class ProductreviewsPageView(TemplateView):
    template_name = "product-reviews.html"
class ReviewPageView(TemplateView):
    template_name = "review.html"
class ProfilePageView(TemplateView):
    template_name = "profile.html"