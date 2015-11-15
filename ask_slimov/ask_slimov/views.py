# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response

from ask_slimov import helpers
from ask_slimov.models import Question, Answer, QuestionLike, Tag
from django.contrib.auth.models import User

# new questions
def questions_new(request):
    questions = Question.objects.list_new()

    pagination = helpers.paginate(questions, request)
    return render(request, 'questions_list.html',
            {
                'questions': pagination,
                'title': 'Новые вопросы',
                'key': 'new',
            })

# hot questions
def questions_hot(request):
    questions = Question.objects.list_hot()

    pagination = helpers.paginate(questions, request)
    return render(request, 'questions_list.html',
            {
                'questions': pagination,
                'title': 'Лучшие вопросы',
                'key': 'hot',
            })

# questiong by tag
def questions_tag(request, tag):
    try:
        tag = Tag.objects.get_by_title(tag)
    except Tag.DoesNotExist:
        raise Http404()
    
    questions = Question.objects.list_tag(tag)

    pagination = helpers.paginate(questions, request)
    return render(request, 'questions_list.html',
            {
                'questions': pagination,
                'title': u'Тег ' + tag.title,
            })

# single question
def question(request, id):
    try:
        q = Question.objects.get_single(int(id))
    except Question.DoesNotExist:
        raise Http404

    return render(request, 'question.html', {
                'question': q,
            })

# login form
def form_login(request):
    return render(request , 'form_login.html', {})

# register form
def form_signup(request):
    return render(request , 'form_signup.html', {})

# new question form
def form_question_new(request):
    return render(request , 'form_question_new.html', {})

def info(request):
    to_show = [
        ['GET - параметры', request.GET],
        ['POST - параметры', request.POST]
    ]

    output = ['<html>', '<h1>%s</h1>' % 'Привет, мир!']

    for params in to_show:
        output.append('<h3>%s (%d)</h3>'
                % (params[0], len(params[1])))
        output.append('<pre>')

        output.extend(
            [
                "%s ==> '%s' \n"
                    % (k, v) for k,v in params[1].items()
            ]
        )

        output.append('</pre>')

    output.append('</html>')

    output.append('</html>')
    return HttpResponse(output)
