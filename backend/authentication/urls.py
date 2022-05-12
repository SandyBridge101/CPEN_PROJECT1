from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.landing_page,name="home"),
    #path('register/',views.register,name="auth-register"),
    #path("signup/", views.register.as_view(), name="signup"),
    path('register/', views.register, name='register'),
    path('nav/', views.base, name='nav'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]


