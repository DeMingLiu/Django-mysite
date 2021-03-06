# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, Http404
from .models import Question

from django.template import RequestContext, loader
# Create your views here.
def index(request):
    latest_question_list = Question.objcets.order_by('-pub_date')[:5]
    # output = ', '.join([p.question_text for p in latest_question_list])
    # template = loader.gettemplate('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_question_list' : latest_question_list,
    #     })
    context = {'latest_question_list' : latest_question_list}
    return render(request,'polls.index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
        return reder(request, 'polls.detail.html',{'qeustion': question})


    return HttpResponse("You are looking at qeustion %s." % question_id)

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on qeustion %s. " % question_id)