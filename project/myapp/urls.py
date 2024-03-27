from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic_comments, name='topic_comments'),
    # Add other URL patterns as needed
]
