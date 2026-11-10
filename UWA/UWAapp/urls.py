from django.urls import path

from . import views

app_name = 'UWAapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.page, {'slug': 'about'}, name='about'),
    path('conservation/', views.page, {'slug': 'conservation'}, name='conservation'),
    path('plan-your-visit/', views.page, {'slug': 'plan'}, name='plan'),
    path('destinations/', views.destinations, name='destinations'),
    path('destinations/<slug:slug>/', views.destination_detail, name='destination-detail'),
    path('contact/', views.contact, name='contact'),
]
