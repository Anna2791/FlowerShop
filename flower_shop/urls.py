from django.urls import path
from flower_shop import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('catalog/', views.catalog, name='catalog'),
    path('order/<int:flower_id>/', views.order, name='order'),
    path('profile/', views.profile, name='profile'),
    # Можно добавить путь по умолчанию:
    path('', views.catalog, name='home'),
]
