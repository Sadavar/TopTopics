
from django.shortcuts import render
from django.http import HttpResponse
import requests
import praw
from .models import Greeting


# Create your views here.
def index(request):

    reddit = praw.Reddit(client_id='PqeRHaJrQIdEQg', client_secret='rtA7jHjPB9x3cpDsaXKES-G2Tt8', user_agent='Linux:TopTopics:v0.0.1 (by /u/ModsAreKindaGay)')
    topic_list = []
    topic_urls = []
    topic_and_url = {}
    x = 0

    for submission in reddit.subreddit('technews').hot(limit=12):
        topic_list.append(submission.title)
        topic_urls.append(submission.url)
        topic_and_url[topic_list[x]] = topic_urls[x]
        x += 1

    #return render(request, 'index.html', {'topics': topic_and_url})
    return render(request, 'index.html', {"topic_and_url": topic_and_url})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
