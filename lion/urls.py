from django.urls import path
from . import views


urlpatterns = [
    path('<int:lion_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]