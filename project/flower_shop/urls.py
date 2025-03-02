from django.urls import path
from .views import register, catalog, order, profile

urlpatterns = [
    path('', catalog, name='home'),  # Главная страница теперь ведет на каталог
    path('register/', register, name='register'),
    path('catalog/', catalog, name='catalog'),
    path('order/<int:flower_id>/', order, name='order'),
    path('profile/', profile, name='profile')
]
