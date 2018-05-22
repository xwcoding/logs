from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry  # import model to register
admin.site.register(Topic)              # manage model through the admin site
admin.site.register(Entry)