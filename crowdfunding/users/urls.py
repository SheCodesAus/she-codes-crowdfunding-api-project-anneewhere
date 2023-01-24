from django.urls import path

from . import views

urlpatterns = [
 path('', views.CustomUserList.as_view(), name='customuser-list'),
 path('<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),
 path('changepassword/', views.ChangePasswordView.as_view(), name='change-password')
]