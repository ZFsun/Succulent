from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
import json
import time
# Create your views here.
def main(request):
    username = request.COOKIES.get('username', '')
    return render(request, 'sucapphtml/main.html', {'username': username})

def index(request):
    mainrandobject = Maintain.objects.order_by('?')[0:5]
    randobject = SucInfo.objects.order_by('?')[0:7]

    return render(request, 'sucapphtml/index.html', {'randsuc': randobject,'mainrandobject': mainrandobject})

def top(request):
    username = request.COOKIES.get('username', '')
    return render(request, 'sucapphtml/top.html', {'username': username})

def left(request):
    username = request.COOKIES.get('username', '')
    return render(request, 'sucapphtml/left.html', {'username': json.dumps(username)})

def handbook(request):
    familylist = FamilyGenus.objects.values('family').distinct()
    genuslist = FamilyGenus.objects.values('genus').distinct()

    return render(request, 'sucapphtml/handbook.html', {'familylist':familylist, 'genuslist':genuslist})

def ihandbook(request, currentpage=1):

    family = request.GET.get('family', '')
    genus = request.GET.get('genus', '')
    searchinfo = request.GET.get('search_info', '')
    # print('******')
    # print([family,genus])
    list1 = SucInfo.objects.all().order_by("id")
    if family != '':
        list1 = SucInfo.objects.filter(family=family)
    if genus != '':
        list1 = SucInfo.objects.filter(genus=genus)
    if searchinfo:
        list1 = SucInfo.objects.filter(name__contains=searchinfo)

    # print(list1)
    p = Paginator(list1, 12)
    currentpage = int(currentpage)
    totalpages = p.num_pages
    list2 = p.page(currentpage)
    plist = p.page_range
    return render(request, 'sucapphtml/ihandbook.html', {'pageobject': list2, 'plist': plist, 'currentpage': currentpage, 'totalpages': totalpages})

def getgenus(request):
    family = request.GET.get('fam')
    # print('*********')
    # print(family)
    fg = FamilyGenus.objects.filter(family=family)
    fg2 = []
    for i in fg:
        fg2.append(i.genus)
    return JsonResponse({'data': fg2})
    # return render(request, 'sucapphtml/getgenus.html',{'family':family})

def sucdetail(request, id):
    infoid = SucInfo.objects.filter(id=id)
    return render(request, 'sucapphtml/sucdetail.html', {'infoid': infoid})

def maintenance(requset, pageindex=1):
    list = Maintain.objects.all().order_by('-editDate')
    randobject = Maintain.objects.order_by('?')[0:4]
    p = Paginator(list, 5)
    pageindex = int(pageindex)
    totalpages = p.num_pages
    pagelist = p.page(pageindex)
    pageindexlist = p.page_range
    return render(requset, 'sucapphtml/maintenance.html', {'pageobject': pagelist, 'plist': pageindexlist, 'currentpage': pageindex, 'totalpages': totalpages, 'randobject': randobject})

def maindetail(request, id):
    maininfo = Maintain.objects.filter(id=id)
    return render(request, 'sucapphtml/maindetail.html', {'maininfo': maininfo})

def mainedit(request):
    return render(request, 'sucapphtml/mainedit.html')

def editsave(request):
    maintain = Maintain()
    maintain.author = request.COOKIES.get('username', '')
    maintain.editDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
    maintain.title = request.POST.get('title', '')
    maintain.content = request.POST.get('content', '')
    if maintain.title != '' and maintain.content != '':
        maintain.save()
    return render(request, 'sucapphtml/mainedit.html')
