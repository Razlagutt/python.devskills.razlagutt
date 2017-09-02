from django.conf.urls import url
from testurlapp import views


urlpatterns = [
    url(r'^$', views.home, name='home')
]
