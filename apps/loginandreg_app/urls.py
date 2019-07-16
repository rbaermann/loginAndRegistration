from django.conf.urls import url
from . import views
                
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg$', views.reg),
    url(r'^login$', views.log),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]