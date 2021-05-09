from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path('register-user', views.register_view, name="register"),
    path('login-user', views.login_view, name="login"),
    path('logout-user', views.logout_view, name="logout"),
]
