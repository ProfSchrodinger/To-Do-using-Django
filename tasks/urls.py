from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutPage, name='logout'),

    path('', views.homePage, name='home'),
    path('create/', views.createPage, name='createPage'),
    path('update/<str:pk>/', views.updatePage, name='updatePage'),
    path('delete/<str:pk>/', views.deletePage, name='deletePage'),

    path('user/', views.userPage, name='userPage'),
]
