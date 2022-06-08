from django.urls import path

from tasks.views import homepage
from . import views

urlpatterns = [
    path('', homepage, name="homepage"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
]
