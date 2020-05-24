from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from vote.models import Subject, Teacher

# Create your views here.

def index(request):
    return HttpResponse('<h1>hello</h1>')

def show_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'subject.html', {'subjects': subjects})

def show_teachers(request):
    try:
        sno = int(request.GET['sno'])
        subject = Subject.objects.get(no=sno)
        teachers = subject.teacher_set.all()
        return render(request, 'teachers.html', {'subject': subject, 'teachers': teachers})
    except (KeyError, ValueError, Subject.DoesNotExist):
        return redirect('/vote') 


def praise_or_criticize(request):
    try:
        tno = int(request.GET['tno'])
        teacher = Teacher.objects.get(no=tno)
        if request.path.startswith('/vote/praise'):
            teacher.good_count += 1
        elif request.path.startswith('/vote/criticize'):
            teacher.bad_count += 1
        else:
            pass
        teacher.save()
        data = {'code': 200, 'hint': u'操作成功'}
    except (KeyError, ValueError, Teacher.DoseNotExist):
        data = {'code': 404, 'hint': u'操作失败'}
    return JsonResponse(data)

