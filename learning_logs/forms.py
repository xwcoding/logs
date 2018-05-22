from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm): # inherit from forms.ModelForm
  class Meta:
    model = Topic                 # what model to base from
    fields = ['text']             # what field to include in the form
    labels = {'text': ''}         # do not generate a label for above text field


class EntryForm(forms.ModelForm):
  class Meta:
    model = Entry
    fields = ['text']
    labels = {'text': ''}
    widgets = {'text': forms.Textarea(attrs={'cols':100})}
    # override Django's default widget definition and customize element