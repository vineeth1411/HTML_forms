from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is Submitted')
    return render(request,'first.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')



    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO = Topic.objects.all()
    d = {'LTO' : LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST['name']
        url=request.POST['url']
        TO = Topic.objects.get(topic_name=tn)
        TO.save()
        WO=WebPage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('topic inserted')
    return render(request,'insert_webpage.html',d)


def retrive_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        print(MSTS)
        RWOS=WebPage.objects.none()

        for i in  MSTS:
            RWOS=RWOS|WebPage.objects.filter(topic_name=i)

        d1={'RWOS':RWOS}
        return render(request,'display_webpages.html',d1)


    return render(request,'retrive_webpage.html',d)



def checkbox(request):
    LTO = Topic.objects.all()
    d = {'LTO' : LTO}
    return render(request,'checkbox.html',d)












