from django.urls import path
from users import views

urlpatterns = [
    path(r'all/', views.user_list_view, name='user_all'),
    path(r'<int:pk>/', views.user_detail_view, name='user_details'),
    path(r'set_password', views.user_set_password, name='user_set_password'),
]
