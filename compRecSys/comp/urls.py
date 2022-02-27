from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view()),
    re_path(r'^category/(\d+)$', views.IndexView.as_view()),
    re_path(r'^category/(\d+)/page/(\d+)$', views.IndexView.as_view()),
    re_path(r'^compdetail/(\d+)$', views.DetailView.as_view()),
]