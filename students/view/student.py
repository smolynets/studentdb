# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student
def students_list(request):
  students = Student.objects.all()
  return render(request, 'students/stud.html', {'students': students})
def stud_add(request):
    return render(request, 'students/stud_add_form.html', {})
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
