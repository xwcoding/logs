from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404    #redirect page
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """home page"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """topics page"""
    topics = Topic.objects.order_by('date_added')
    # topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)
# A context is a
# dictionary in which the keys are names we’ll use in the template to access
# the data and the values are the data we need to send to the template. In this
# case, there’s one key-value pair, which contains the set of topics we’ll display
# on the page. When building a page that uses data, we pass the context variable
# to render() as well as the request object and the path to the template 

@login_required
def topic(request, topic_id):
    """topic page"""
    topic = Topic.objects.get(id=topic_id)
    # make sure topic belongs to its owner
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):         # submit form and return to topics page
    """add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        # GET request to get new form initially
        form = TopicForm()  
    else:
        # POST data submitted; process data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False) # save data to DB
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics')) # return to topics page
    
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """add a new entry"""
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # return an entry object
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id])) # pass topic_id as arg 
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """edit an entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # make sure topic belongs to its owner
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)    # initial request to load entry
    else:
        form = EntryForm(instance=entry, data=request.POST) # load entry to be edited
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context={'entry':entry, 'topic':topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
    