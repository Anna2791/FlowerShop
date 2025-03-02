from django.urls import path
from flower_shop import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('order/<int:flower_id>/', views.order, name='order'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]


