# generate_data.py

from django.utils import timezone 
import random
from faker import Faker
from datetime import datetime
from myapp.models import User, Topic, FavoriteTopic, TopicType, Comment
 
fake = Faker()
 
# Create 10 random users
for _ in range(10):
    User.objects.create(
        username=fake.user_name(),
        name=fake.name(),
        password=fake.password()
    )
 
# Create 10 random topic types
topic_types = ['Technology', 'Science', 'Arts', 'Sports', 'Politics']
for name in topic_types:
    TopicType.objects.create(name=name)
 
# Create 10 random topics
for _ in range(10):
    topic_type = random.choice(TopicType.objects.all())
    Topic.objects.create(
        name=fake.sentence(nb_words=3),
        type=topic_type,
        description=fake.text()
    )
 
# Create 10 random favorite topics for random users
users = User.objects.all()
topics = Topic.objects.all()
for _ in range(10):
    user = random.choice(users)
    topic = random.choice(topics)
    FavoriteTopic.objects.create(user=user, topic=topic)
 
# Create 10 random comments for random topics by random users
for _ in range(10):
    user = random.choice(users)
    topic = random.choice(topics)
    Comment.objects.create(
        user=user,
        topic=topic,
        body=fake.text(),
        timestamp=timezone.now()
    )