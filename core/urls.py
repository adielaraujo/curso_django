
from django.urls import include, path, re_path
from .views import home



urlpatterns = [
    re_path(r'^$', home, name='core_home'),
]