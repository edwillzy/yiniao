import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from all import models

# Create your views here.
from yiniao import settings

def baseInfo(request, pk):
    baseInfo_list = models.personalInfo.objects.get(xm=pk)
    educationExperience_list = models.JYJL.objects.filter(xm=pk)
    workExperience_list = models.GZJL.objects.filter(xm=pk)
    positionExperience_list = models.ZCJL.objects.filter(xm=pk)
    dyRelated_list = models.DY.objects.get(xm=pk)
    myTeaching_list = models.WDJX.objects.filter(xm=pk)
    context = {
        'baseInfo_list': baseInfo_list,
        'educationExperience_list': educationExperience_list,
        'workExperience_list': workExperience_list,
        'positionExperience_list': positionExperience_list, 'dyRelated_list': dyRelated_list,
        'myTeaching_list': myTeaching_list,
        'id': pk
    }
    return render(request, 'BaseInfo.html', context)

def personInfoEdit(request, pk):
    if request.method == 'GET':
        baseInfo_list = models.personalInfo.objects.get(xm=pk)
        context = {'baseInfo_list':baseInfo_list}
        return  render(request, 'BaseInfoEdit1.html', context)
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            file = request.FILES.dict()
            print(file)
            infoDict = dict()
            #print(form)
            for item in form:
                if(item != 'csrfmiddlewaretoken' and form[item] != '' and item != 'save'):
                    t = {item : form[item]}
                    infoDict.update(t)
            infoDict.update(file)
            print(infoDict)
            models.personalInfo.objects.filter(xm = pk).update(**infoDict)
            for item in file:
                print(file[item])
                f_path = os.path.join(settings.MEDIA_ROOT, str(file[item]))
                with open(f_path, 'wb+') as destination:
                    for chunk in file[item].chunks():
                        destination.write(chunk)
            return redirect(baseInfo, pk)
        else:
            return redirect(baseInfo, pk)

#################################################
def eduExpEdit(request, pk1):
    pk2 = request.GET.get('pk')
    if request.method == 'GET':
        educationExperience = models.JYJL.objects.get(xm=pk1, qzsj=pk2)
        context = {'educationExperience': educationExperience}
        return render(request, 'BaseInfoEdit2.html', context)
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            infoDict = dict()
            # print(form)
            for item in form:
                if (item != 'csrfmiddlewaretoken' and form[item] != '' and item != 'save'):
                    t = {item: form[item]}
                    infoDict.update(t)
            print(infoDict)
            models.JYJL.objects.filter(xm=pk1, qzsj=pk2).update(**infoDict)
            return redirect(baseInfo, pk1)
        else:
            return redirect(baseInfo, pk1)

def eduExpDel(request, pk1):
    pk2 = request.GET.get('pk')
    models.JYJL.objects.get(xm=pk1, qzsj=pk2).delete()
    return redirect(baseInfo, pk1)

def eduExpAdd(request, pk):
    if request.method == 'GET':
        return render(request, 'BaseInfoEdit2A.html')
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            del form['csrfmiddlewaretoken']
            del form['save']
            infoDict = dict()
            # print(form)
            for item in form:
                if (form[item] == ''):
                    return HttpResponse("none is existing")
                t = {item: form[item]}
                infoDict.update(t)
            infoDict.update({'xm':pk})
            print(infoDict)
            models.JYJL.objects.create(**infoDict)
            return redirect(baseInfo, pk)
        else:
            return redirect(baseInfo, pk)

#####################
def workExpEdit(request, pk1):
    pk2 = request.GET.get('pk')
    if request.method == 'GET':
        workExperience = models.GZJL.objects.get(xm=pk1, qzsj=pk2)
        context = {'workExperience': workExperience}
        return render(request, 'BaseInfoEdit3.html', context)
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            del form['csrfmiddlewaretoken']
            del form['save']
            infoDict = dict()
            # print(form)
            for item in form:
                if (form[item] != ''):
                    t = {item: form[item]}
                    infoDict.update(t)
            print(infoDict)
            models.GZJL.objects.filter(xm=pk1, qzsj=pk2).update(**infoDict)
            return redirect(baseInfo, pk1)
        else:
            return redirect(baseInfo, pk1)

def workExpDel(request, pk1):
    pk2 = request.GET.get('pk')
    models.GZJL.objects.get(xm=pk1, qzsj=pk2).delete()
    return redirect(baseInfo, pk1)

def workExpAdd(request, pk):
    if request.method == 'GET':
        return render(request, 'BaseInfoEdit3A.html')
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            del form['csrfmiddlewaretoken']
            del form['save']
            infoDict = dict()
            # print(form)
            for item in form:
                if (form[item] == ''):
                    return HttpResponse("none is existing")
                t = {item: form[item]}
                infoDict.update(t)
            infoDict.update({'xm':pk})
            print(infoDict)
            models.GZJL.objects.create(**infoDict)
            return redirect(baseInfo, pk)
        else:
            return redirect(baseInfo, pk)
################################################
def posiExpEdit(request, pk1):
    pk2 = request.GET.get('pk')
    if request.method == 'GET':
        posiExperience = models.ZCJL.objects.get(xm=pk1, sj=pk2)
        context = {'posiExperience': posiExperience}
        return render(request, 'BaseInfoEdit4.html', context)
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            del form['csrfmiddlewaretoken']
            del form['save']
            infoDict = dict()
            # print(form)
            for item in form:
                if (form[item] != ''):
                    t = {item: form[item]}
                    infoDict.update(t)
            print(infoDict)
            models.ZCJL.objects.filter(xm=pk1, sj=pk2).update(**infoDict)
            return redirect(baseInfo, pk1)
        else:
            return redirect(baseInfo, pk1)

def posiExpDel(request, pk1):
    pk2 = request.GET.get('pk')
    models.ZCJL.objects.get(xm=pk1, sj=pk2).delete()
    return redirect(baseInfo, pk1)

def posiExpAdd(request, pk):
    if request.method == 'GET':
        return render(request, 'BaseInfoEdit4A.html')
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            del form['csrfmiddlewaretoken']
            del form['save']
            infoDict = dict()
            # print(form)
            for item in form:
                if (form[item] == ''):
                    return HttpResponse("none is existing")
                t = {item: form[item]}
                infoDict.update(t)
            infoDict.update({'xm':pk})
            print(infoDict)
            models.ZCJL.objects.create(**infoDict)
            return redirect(baseInfo, pk)
        else:
            return redirect(baseInfo, pk)

#####################################
def partEdit(request, pk):
    if request.method == 'GET':
        part = models.DY.objects.get(xm=pk)
        context = {'part': part}
        return render(request, 'BaseInfoEdit5.html', context)
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            del form['csrfmiddlewaretoken']
            del form['save']
            infoDict = dict()
            # print(form)
            for item in form:
                if (form[item] != ''):
                    t = {item: form[item]}
                    infoDict.update(t)
            print(infoDict)
            models.DY.objects.filter(xm=pk).update(**infoDict)
            return redirect(baseInfo, pk)
        else:
            return redirect(baseInfo, pk)

##################################################
def myTeachingEdit(request, pk1):
    pk2 = request.GET.get('pk1')
    pk3 = request.GET.get('pk2')
    if request.method == 'GET':
        myTeaching = models.WDJX.objects.get(xm=pk1, qzsj=pk2, jskc=pk3)
        context = {'myTeaching': myTeaching}
        return render(request, 'BaseInfoEdit6.html', context)
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            del form['csrfmiddlewaretoken']
            del form['save']
            infoDict = dict()
            # print(form)
            for item in form:
                if (form[item] != ''):
                    t = {item: form[item]}
                    infoDict.update(t)
            print(infoDict)
            models.WDJX.objects.filter(xm=pk1, qzsj=pk2, jskc=pk3).update(**infoDict)
            return redirect(baseInfo, pk1)
        else:
            return redirect(baseInfo, pk1)

def myTeachingDel(request, pk1):
    pk2 = request.GET.get('pk1')
    pk3 = request.GET.get('pk2')
    models.WDJX.objects.get(xm=pk1, qzsj=pk2, jskc=pk3).delete()
    return redirect(baseInfo, pk1)

def myTeachingAdd(request, pk):
    if request.method == 'GET':
        return render(request, 'BaseInfoEdit6A.html')
    else:
        if 'save' in request.POST:
            form = request.POST.dict()
            del form['csrfmiddlewaretoken']
            del form['save']
            infoDict = dict()
            # print(form)
            for item in form:
                if (form[item] == ''):
                    return HttpResponse("none is existing")
                t = {item: form[item]}
                infoDict.update(t)
            infoDict.update({'xm':pk})
            print(infoDict)
            models.WDJX.objects.create(**infoDict)
            return redirect(baseInfo, pk)
        else:
            return redirect(baseInfo, pk)