from django.shortcuts import render

from topic.models import Redactor, Topic, Newspaper


def index(request):
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topic": num_topics,
    }

    return render(request, "topic/index.html", context)
