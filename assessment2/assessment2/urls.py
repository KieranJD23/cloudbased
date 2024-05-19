from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static 
from . import settings 
from django.views.generic.base import TemplateView



urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", TemplateView.as_view(template_name="product.html"), name="product"),
    path("data/", include("django.contrib.auth.urls")),
    path("data/", include("data.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
