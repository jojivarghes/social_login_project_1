from django.urls import path
from users import views

urlpatterns = [
    path('all/', views.user_list_view, name='user_all'),
    path('<int:pk>/', views.user_detail_view, name='user_details'),
    path('set_password/', views.ChangePasswordView.as_view()),
    path('search/', views.search, name='user_search')
]
