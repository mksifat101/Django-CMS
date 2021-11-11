from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.category, name='category'),
    path('<slug:category_slug>/<slug:post_slug>/', views.single, name='single'),
]
