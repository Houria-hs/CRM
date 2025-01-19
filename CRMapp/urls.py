from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home' ),
    path('register/', views.register , name='register' ),
    path('logout/', views.logout_view , name='logout' ),
    path('customer_record/<int:pk>/ ', views.customer_record , name='customer_record' ),
    path('Delete_record/<int:pk>/', views.Delete_record , name='Delete_record' ),
    path('Add_record/', views.Add_record , name='Add_record' ),
    path('update_record/<int:pk>/ ', views.update_record , name='update_record' ),
]