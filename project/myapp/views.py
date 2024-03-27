# views.py
from django.shortcuts import render
from .models import User, Topic, FavoriteTopic, TopicType, Comment
 
def home(request):

    models = [User, Topic, FavoriteTopic, TopicType, Comment]
    return render(request, "home.html", {"models": models})

def topics(request):
    topics = Topic.objects.all()
    return render(request, 'topics.html', {'topics': topics})

def topic_comments(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    comments = Comment.objects.filter(topic=topic)
    return render(request, 'topic_comments.html', {'topic': topic, 'comments': comments})