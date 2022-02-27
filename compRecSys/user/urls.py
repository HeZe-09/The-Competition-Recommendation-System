from django.urls import re_path
from . import views


urlpatterns=[
    re_path(r'^register/$',views.RegisterView.as_view()),
    re_path(r'^checkUname/$',views.CheckUnameView.as_view()),
    re_path(r'^center/$', views.CenterView.as_view()),
    re_path(r'^logout/$', views.LogoutView.as_view()),
    re_path(r'^login/$', views.LoginView.as_view()),
    re_path(r'^loadCode.jpg$', views.LoadCodeView.as_view()),
    re_path(r'^checkCode/$', views.CheckCodeView.as_view()),
]