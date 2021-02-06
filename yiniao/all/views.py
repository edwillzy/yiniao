from all import models
from django.shortcuts import render, redirect


# Create your views here.
def getAll(request):
    baseInfo_list = models.personalInfo.objects.all().first()
    educationExperience_list = models.JYJL.objects.all()
    workExperience_list = models.GZJL.objects.all()
    positionExperience_list = models.ZCJL.objects.all()
    dyRelated_list  =models.DY.objects.all().first()
    myTeaching_list = models.WDJX.objects.all()
    paper_list = models.LW.objects.all()
    hProject_list = models.HXXM.objects.all().first()
    vProject_list = models.ZXXM.objects.all().first()
    patent_list = models.ZL.objects.all().first()
    sCopyRight_list  = models.RJZZQ.objects.all().first()
    works_list = models.ZZ.objects.all().first()
    otherWorks_list = models.QTCG.objects.all().first()
    prize_list = models.HJQK.objects.all().first()
    honor_list = models.RYCH.objects.all().first()
    myStudents_list = models.WDXS.objects.all().first()
    return render(
        request,
        'HomePage.html',
        {
            'baseInfo_list': baseInfo_list,
            'educationExperience_list': educationExperience_list,
            'workExperience_list': workExperience_list,
            'positionExperience_list':positionExperience_list,
            'dyRelated_list':dyRelated_list,
            'myTeaching_list':myTeaching_list,
            'paper_list':paper_list,
            'hProject_list':hProject_list,
            'vProject_list':vProject_list,
            'patent_list':patent_list,
            'sCopyRight_list':sCopyRight_list,
            'works_list':works_list,
            'otherWorks_list':otherWorks_list,
            'prize_list':prize_list,
            'honor_list':honor_list,
            'myStudents_list':myStudents_list,

        }
    )
def getBaseInfo(request):
    baseInfo_list = models.personalInfo.objects.all().first()
    educationExperience_list = models.JYJL.objects.all()
    workExperience_list = models.GZJL.objects.all()
    positionExperience_list = models.ZCJL.objects.all()
    dyRelated_list = models.DY.objects.all().first()
    myTeaching_list = models.WDJX.objects.all()
    return render(
        request,
        'BaseInfo.html',
        {
            'baseInfo_list': baseInfo_list,
            'educationExperience_list': educationExperience_list,
            'workExperience_list': workExperience_list,
            'positionExperience_list': positionExperience_list,
            'dyRelated_list': dyRelated_list,
            'myTeaching_list': myTeaching_list
        }
    )
def getHonor(request):
    prize_list = models.HJQK.objects.all()
    honor_list = models.RYCH.objects.all()
    return render(
        request,
        'Honor.html',
        {
            'prize_list':prize_list,
            'honor_list':honor_list
        }
    )
def getStudent(request):
    myStudents_list = models.WDXS.objects.all()
    return render(
        request,
        'MyStudent.html',
        {
            'myStudents_list':myStudents_list
        }
    )
def getPaper(request):
    paper_list = models.LW.objects.all()
    return render(
        request,
        'Paper.html',
        {
            'paper_list':paper_list
        }
    )
def getPatent(request):
    patent_list = models.ZL.objects.all()
    sCopyRight_list = models.RJZZQ.objects.all()
    works_list = models.ZZ.objects.all()
    otherWorks_list = models.QTCG.objects.all()
    return render(
        request,
        'Patent.html',
        {
            'patent_list': patent_list,
            'sCopyRight_list':sCopyRight_list,
            'works_list':works_list,
            'otherWorks_list':otherWorks_list,
        }

    )
def getProject(request):
    hProject_list = models.HXXM.objects.all()
    vProject_list = models.ZXXM.objects.all()
    return render(
        request,
        'Project.html',
        {
            'hProject_list':hProject_list,
            'vProject_list':vProject_list,
        }
    )
def editInfo(request):
    if request.method == 'GET':
        baseInfo_list = models.personalInfo.objects.all().first()
        paper_list = models.LW.objects.all()
        vProject_list = models.ZXXM.objects.all().first()
        return render(
            request,
            'InformationEdit.html',
            {
                'baseInfo_list': baseInfo_list,
                'paper_list':paper_list,
                'vProject_list':vProject_list
            }


        )
    elif request.method == 'POST':
        xm = request.POST.get('xm')
        xb = request.POST.get('xb')
        lxdh = request.POST.get('lxdh')
        email = request.POST.get('email')
        info_bz = request.POST.get('bz')
        models.personalInfo.objects.first().update(xm=xm,xb=xb,lxdh=lxdh,email=email,bz=info_bz)
        xmmc = request.POST.get('v')
        xmjf = request.POST.get('xmjf')
        kssj = request.POST.get('kssj')
        jhwcrq = request.POST.get('jhwcrq')
        models.ZXXM.objects.first().update(xmmc=xmmc,xmjf=xmjf,kssj=kssj,jhwcrq=jhwcrq)
        return redirect('/HomePages.html')