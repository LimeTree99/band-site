from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from about.models import page

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=page.objects.get(pk=1),
        template_name="about/main.html"
    ))
]
