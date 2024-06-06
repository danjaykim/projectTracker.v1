from django.urls import path
from faces.views import homepage, contact, about


urlpatterns = [
    path("", homepage, name="homepage"),
    path("contact/", contact, name="contact_page"),
    path("about/", about, name="about_page"),
]
