from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.register, name='register'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
