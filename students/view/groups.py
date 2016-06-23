# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
def grup(request):
    return render(request, 'students/grup.html', {})
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)
def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
