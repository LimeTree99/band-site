from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from home_page.models import Gig

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=Gig.objects.all().order_by('-date'),
        template_name="home_page/home.html"
    ))
]
