from django.urls import path
from twitter_data.views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]