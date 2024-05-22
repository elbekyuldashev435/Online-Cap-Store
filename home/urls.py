from django.urls import path
from .views import home_page, AboutView


app_name = 'home'
urlpatterns = [
    path('', home_page, name='home-page'),
    path('about/', AboutView.as_view(), name='about'),
    ]