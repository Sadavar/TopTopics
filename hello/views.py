from django.shortcuts import render
from django.http import HttpResponse
import requests
import praw
from .models import Greeting


# Create your views here.
def index(request):

    reddit = praw.Reddit(client_id='PqeRHaJrQIdEQg', client_secret='rtA7jHjPB9x3cpDsaXKES-G2Tt8', user_agent='Linux:TopTopics:v0.0.1 (by /u/ModsAreKindaGay)')
    topics = []
    topics2 = []
    for submission in reddit.subreddit('technews').hot(limit=10):
    	topics.append(submission.title)

    for number, topic in enumerate(topics, 1):
    	topics2.append(str(number) + '. ' + topic)


	#for number, topic in enumerate(topics, 1):
	#	print(str(number) + '.', topic)

    return HttpResponse('<pre>' + '<h1 style="color:black; text-align:center; font-size: 50px;"> TopTopics: Tech News</h1>' + str(topics2[0]) + "\n" +  "\n" + str(topics2[1]) + "\n" + "\n" + str(topics2[2]) + "\n" + "\n" + str(topics2[3]) + "\n" + "\n" + str(topics2[4]) + "\n" + "\n" + str(topics2[5]) + "\n" + "\n" + str(topics2[6]) + "\n" + "\n" + str(topics2[7]) + "\n" + "\n" + str(topics2[8]) + "\n" + "\n" + str(topics2[9]) + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
