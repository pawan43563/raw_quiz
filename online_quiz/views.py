from django.shortcuts import render
from .models import *
from .forms import *
import random
import ast
from datetime import datetime
from django.http import HttpResponse
 

def Rules(request):
    template_name = 'online_quiz/rules.html'
    return render(request, template_name)



def Welcome(request):
    template_name = 'online_quiz/login.html'
    return render(request, template_name)


def cache1(request):
    template_name = 'online_quiz/quiz.html'
    l=[random.randrange(1,21,1)]
    n=5
    i=0
    while i!=n:
        temp=random.randrange(1,21,1) 
        if temp not in l:
            l.append(temp)
        i+=1
    # start_time=datetime.now()
    
    q1=Question.objects.get(id=l[0])
    q2=Question.objects.get(id=l[1])
    q3=Question.objects.get(id=l[2])
    q4=Question.objects.get(id=l[3])
    q5=Question.objects.get(id=l[4])
    # timer={}
    response=render(request,template_name,{"q1":q1,"q2":q2,"q3":q3,"q4":q4,"q5":q5})
    # response.set_cookie('start_time',datetime.now())
    
    return response

def cache3(request):

    qno1=request.POST['qno1']
    
    qno2=request.POST['qno2']
    qno3=request.POST['qno3']
    qno4=request.POST['qno4']
    qno5=request.POST['qno5']
    
    try:
        qans1=request.POST['choice_pk1']
    except:
        pass
    try:
        qans2=request.POST['choice_pk2']
    except:
        pass
    try:
        qans3=request.POST['choice_pk3']
    except:
        pass
    try:
        qans4=request.POST['choice_pk4']
    except:
        pass
    try:
        qans5=request.POST['choice_pk5']
    except:
        pass

    ql=Question.objects.get(id=qno1)
    ans1=ql.answer_set.all()[0]
    q2=Question.objects.get(id=qno2)
    ans2=q2.answer_set.all()[0]
    q3=Question.objects.get(id=qno3)
    ans3=q3.answer_set.all()[0]
    q4=Question.objects.get(id=qno4)
    ans4=q4.answer_set.all()[0]
    q5=Question.objects.get(id=qno5)
    ans5=q5.answer_set.all()[0]
    score=0
    try:
        if qans1==ans1.answer:
            score+=1
    except:
        pass
    try:
        if qans2==ans2.answer:
            score+=1
    except:
        pass
    try:
        if qans3==ans3.answer:
            score+=1
    except:
        pass
    try:
        if qans4==ans4.answer:
            score+=1
    except:
        pass
    try:
        if qans5==ans5.answer:
            score+=1
    except:
        pass
    
    
    return render(request,'online_quiz/score.html',{"score":score})