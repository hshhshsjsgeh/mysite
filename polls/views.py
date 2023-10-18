"""
views
"""
from django.shortcuts import render
from django.http import HttpResponse, Http404
# from django.template import loader

from .models import Question

# Create your views here.

def index(request):
    """
    index page
    """
    # last_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in last_question_list])
    # return HttpResponse(output)
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'last_question_list': last_question_list,
    }
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """
    detail page
    """
    # print(request.method)
    # return HttpResponse(f'You\'re looking at question {question_id}.')
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404('Question doesn\'t exist')
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    results page
    """
    print(request.method)
    response = f'You\'re looking at the results of question {question_id}.'
    return HttpResponse(response)

def vote(request, question_id):
    """
    vote page
    """
    print(request.method)
    return HttpResponse(f'You\'re voting on question {question_id}.')
