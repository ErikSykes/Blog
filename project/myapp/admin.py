from django.contrib import admin
from .models import User, Topic, FavoriteTopic, TopicType, Comment

class TopicTypeAdmin(admin.ModelAdmin):
    pass  # You can customize this further if needed

admin.site.register(Topic)
admin.site.register(TopicType, TopicTypeAdmin)
admin.site.register(User)