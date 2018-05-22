from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
  """log out user"""
  logout(request)
  return HttpResponseRedirect(reverse('users:login'))

def register(request):
  """register a user"""
  if request.method != 'POST':
    form = UserCreationForm()
  else:
    form = UserCreationForm(data=request.POST)

    if form.is_valid():
      # save user
      new_user = form.save() # return a user object
      # log in and redirect to index page
      authenticate_user = authenticate(username=new_user, # return authenticated user object
        password=request.POST['password1']) # password1 should be the value of 1st input
      login(request, authenticate_user)
      return HttpResponseRedirect(reverse('learning_logs:index'))

  context = {'form': form}
  return render(request, 'users/register.html', context)