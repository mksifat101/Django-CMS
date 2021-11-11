from django.urls import path
from pages import views
import pages

urlpatterns = [
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
]
