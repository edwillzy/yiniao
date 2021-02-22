from django.http import HttpResponse
from django.shortcuts import render, redirect
from all import models
# Create your views here.


def paperInfo(request, fk):
    paper_list = models.LW.objects.filter(zzqc__contains=fk)
    context = {'paper_list':paper_list,
               'id':fk}
    return render(request, "Paper.html",context)

def paperEdit(request, fk):
    pk = request.GET.get('pk')
    if request.method == 'GET':
        paper = models.LW.objects.get(lwjc=pk)
        context = {'paper': paper}
        return render(request, 'PaperE.html', context)
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
            models.LW.objects.filter(lwjc=pk).update(**infoDict)
            return redirect(paperInfo, fk)
        else:
            return redirect(paperInfo, fk)

def paperDel(request, fk):
    pk = request.GET.get('pk')
    models.LW.objects.get(lwjc=pk).delete()
    return redirect(paperInfo, fk)

def paperAdd(request, fk):
    if request.method == 'GET':
        return render(request, 'PaperA.html')
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
            print(infoDict)
            models.LW.objects.create(**infoDict)
            return redirect(paperInfo, fk)
        else:
            return redirect(paperInfo, fk)
