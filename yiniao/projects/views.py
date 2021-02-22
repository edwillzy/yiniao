import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from all import models

# Create your views here.
from yiniao import settings

def projectInfo(request, fk):
    hProject_list = models.HXXM.objects.filter(qtcy__contains=fk)
    vProject_list = models.ZXXM.objects.filter(xmzqtcy__contains=fk)
    context = {'hProject_list':hProject_list,
               'vProject_list':vProject_list,
               'id':fk}
    return render(request, "Project.html",context)

def projectHEdit(request, fk):
    pk = request.GET.get('pk')
    if request.method == 'GET':
        hProject = models.HXXM.objects.get(xmjc=pk)
        context = {'hProject': hProject}
        return render(request, 'Project1.html', context)
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            file = request.FILES.dict()
            print(file)
            infoDict = dict()
            # print(form)
            for item in form:
                if (item != 'csrfmiddlewaretoken' and form[item] != '' and item != 'save'):
                    t = {item: form[item]}
                    infoDict.update(t)
            infoDict.update(file)
            print(infoDict)
            models.HXXM.objects.filter(xmjc=pk).update(**infoDict)
            for item in file:
                print(file[item])
                f_path = os.path.join(settings.MEDIA_ROOT, str(file[item]))
                with open(f_path, 'wb+') as destination:
                    for chunk in file[item].chunks():
                        destination.write(chunk)
            return redirect(projectInfo, fk)
        else:
            return redirect(projectInfo, fk)

def projectHDel(request, fk):
    pk = request.GET.get('pk')
    models.HXXM.objects.get(xmjc=pk).delete()
    return redirect(projectInfo, fk)

def projectHAdd(request, fk):
    if request.method == 'GET':
        return render(request, 'Project1A.html')
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            file = request.FILES.dict()
            del form['csrfmiddlewaretoken']
            del form['save']
            infoDict = dict()
            infoDict.update(file)
            # print(form)
            for item in form:
                if (form[item] == ''):
                    return HttpResponse("none is existing")
                t = {item: form[item]}
                infoDict.update(t)
            print(infoDict)
            models.HXXM.objects.create(**infoDict)
            for item in file:
                print(file[item])
                f_path = os.path.join(settings.MEDIA_ROOT, str(file[item]))
                with open(f_path, 'wb+') as destination:
                    for chunk in file[item].chunks():
                        destination.write(chunk)
            return redirect(projectInfo, fk)
        else:
            return redirect(projectInfo, fk)

def projectVEdit(request, fk):
    pk = request.GET.get('pk')
    if request.method == 'GET':
        vProject = models.ZXXM.objects.get(xmjc=pk)
        context = {'vProject': vProject}
        return render(request, 'Project2.html', context)
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            file = request.FILES.dict()
            print(file)
            infoDict = dict()
            # print(form)
            for item in form:
                if (item != 'csrfmiddlewaretoken' and form[item] != '' and item != 'save'):
                    t = {item: form[item]}
                    infoDict.update(t)
            infoDict.update(file)
            print(infoDict)
            models.ZXXM.objects.filter(xmjc=pk).update(**infoDict)
            for item in file:
                print(file[item])
                f_path = os.path.join(settings.MEDIA_ROOT, str(file[item]))
                with open(f_path, 'wb+') as destination:
                    for chunk in file[item].chunks():
                        destination.write(chunk)
            return redirect(projectInfo, fk)
        else:
            return redirect(projectInfo, fk)

def projectVDel(request, fk):
    pk = request.GET.get('pk')
    models.ZXXM.objects.get(xmjc=pk).delete()
    return redirect(projectInfo, fk)

def projectVAdd(request, fk):
    if request.method == 'GET':
        return render(request, 'Project2A.html')
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            file = request.FILES.dict()
            del form['csrfmiddlewaretoken']
            del form['save']
            infoDict = dict()
            infoDict.update(file)
            # print(form)
            for item in form:
                if (form[item] == ''):
                    return HttpResponse("none is existing")
                t = {item: form[item]}
                infoDict.update(t)
            print(infoDict)
            models.ZXXM.objects.create(**infoDict)
            for item in file:
                print(file[item])
                f_path = os.path.join(settings.MEDIA_ROOT, str(file[item]))
                with open(f_path, 'wb+') as destination:
                    for chunk in file[item].chunks():
                        destination.write(chunk)
            return redirect(projectInfo, fk)
        else:
            return redirect(projectInfo, fk)