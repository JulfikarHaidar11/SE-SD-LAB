from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('create_tweet/', views.create_tweet, name='create_tweet'),
    path('delete_tweet/<int:tweet_id>/', views.delete_tweet, name='delete_tweet'),
]
