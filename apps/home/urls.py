from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

#from admin_volt import views

urlpatterns = [
    # Index
    path('home/dashboard/', login_required(Dashboard.as_view()), name="dashboard"),
    path('', login_view, name="login"),
    path('accounts/logout/', login_required(logout_view), name="logout"),

]