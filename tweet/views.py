from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Tweet
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def index(request):
    tweets = Tweet.objects.all()
    return render(request, 'index.html', {'tweets': tweets})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'signup.html')

def create_tweet(request):
    if request.method == 'POST':
        text = request.POST['text']
        image = request.FILES['image'] if 'image' in request.FILES else None
        tweet = Tweet(user=request.user, text=text, image=image)
        tweet.save()
        return redirect('index')
    return HttpResponse("Method not allowed", status=405)

def delete_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if tweet.user == request.user:
        tweet.delete()
    return redirect('index')
