"""define URL patterns for learning_logs"""

from django.conf.urls import url
from . import views     #import views in the same directory

urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'),
    # r: raw string
    # ^: url starts
    # $: url ends
    # r'^$': means nothing between start and end of the url 
    # views.index: index is a function to call
    # name: for other sections/pages to refer to

    # Show all topics
    url(r'^topics/$', views.topics, name='topics'),

    # detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # page to add a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # edit an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
]