
from django.urls import include, path, re_path
from .views import (
    website_home, 
    website_servicos,
    website_sobre,
    website_planos,
    website_contato,
)


urlpatterns = [
    re_path(r'^$', website_home, name='website_home'),
    re_path(r'^servicos/', website_servicos, name='website_servicos'),
    re_path(r'^sobre/', website_sobre, name='website_sobre'),
    re_path(r'^planos/', website_planos, name='website_planos'),
    re_path(r'^contato/', website_contato, name='website_contato'),
]