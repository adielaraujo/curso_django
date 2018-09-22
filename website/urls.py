
from django.urls import include, path, re_path
from .views import website_home


urlpatterns = [
    re_path(r'^$', website_home, name='website_home'),
]