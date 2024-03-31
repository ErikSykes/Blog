# views.py
from .models import User, Topic, FavoriteTopic, TopicType, Comment
from .forms import CommentForm  # Import the form for adding comments
from django.shortcuts import redirect

 
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


def topic_view(request, topic_id):
    # Your view logic to fetch the topic and related data
    topic = Topic.objects.get(id=topic_id)
    # Pass the topic_id to the template
    return render(request, 'topic_comments.html', {'topic_id': topic_id, 'topic': topic})

def topic_comments(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    comments = Comment.objects.filter(topic=topic)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.topic = topic
            new_comment.save()
            return redirect('topic_comments', topic_id=topic_id)
    else:
        form = CommentForm()

    return render(request, 'topic_comments.html', {'topic': topic, 'comments': comments, 'form': form})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create a new comment object but don't save it yet
            new_comment = form.save(commit=False)
            new_comment.user = request.user  # Assuming the current user is adding the comment
            new_comment.save()  # Save the comment to the database
            return redirect('topic_comments', topic_id=new_comment.topic_id)  # Redirect to the topic page
    else:
        # Handle the case when the request method is not POST
        # This could include displaying an error message or redirecting to another page
        pass