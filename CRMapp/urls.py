from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home' ),
    path('register/', views.register , name='register' ),
    path('logout/', views.logout_view , name='logout' ),
    path('customer_record/<int:pk>/ ', views.customer_record , name='customer_record' ),
]