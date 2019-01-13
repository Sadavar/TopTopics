
from django.shortcuts import render
from django.http import HttpResponse
import requests
import praw
from .models import Greeting


# Create your views here.
def index(request):

    reddit = praw.Reddit(client_id='PqeRHaJrQIdEQg', client_secret='rtA7jHjPB9x3cpDsaXKES-G2Tt8', user_agent='Linux:TopTopics:v0.0.1 (by /u/ModsAreKindaGay)')
    topic_list1 = []
    for submission in reddit.subreddit('technews').hot(limit=12):
    	topic_list1.append(submission.title)

    return render(request, 'index.html', {'topics': topic_list1})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
