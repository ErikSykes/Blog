from myapp.models import User, Topic, FavoriteTopic, TopicType, Comment
 
# Check the number of records in each table
print("Number of users:", User.objects.count())
print("Number of topics:", Topic.objects.count())
print("Number of favorite topics:", FavoriteTopic.objects.count())
print("Number of topic types:", TopicType.objects.count())
print("Number of comments:", Comment.objects.count())
 
# Check if specific data exists
if User.objects.filter(username='example_username').exists():
    print("User with username 'example_username' exists.")
 
 
 
# Function to print data from each table
def print_table_data(model, fields=None):
    print(f"\nData in {model.__name__}:")
    queryset = model.objects.all()
    if fields:
        for obj in queryset:
            print({field: getattr(obj, field) for field in fields})
    else:
        for obj in queryset:
            print(obj.__dict__)
 
# Print data from each table
print_table_data(User, fields=['id', 'username', 'name'])
print_table_data(Topic, fields=['id', 'name', 'type_id', 'description'])
print_table_data(FavoriteTopic, fields=['user_id', 'topic_id'])
print_table_data(TopicType, fields=['id', 'name'])
print_table_data(Comment, fields=['id', 'user_id', 'topic_id', 'body', 'timestamp'])