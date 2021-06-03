from django.shortcuts import render, redirect
from basic_app import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
   return render(request, 'basic_app/index.html') 

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html') 
"""
def register(request):
	if request.method == "POST":
		form = forms.UserProfileInfoForm(request.POST)
	form = forms.UserProfileInfoForm()
	return render(request, 'basic_app/register.html', {'form':form}) 
  """ 

def register(request):
    if request.method == 'POST':
        form = forms.UserProfileInfoForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = forms.UserProfileInfoForm(username=username, password=password)
            login(request, user)
            return redirect('basic_app/index.html')
    else:
        form = forms.UserProfileInfoForm()
    return render(request, 'basic_app/register.html', {'form': form})    