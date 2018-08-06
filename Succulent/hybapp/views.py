from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def forecast(fid, mid):
    fobject = SucInfo.objects.filter(id=fid)
    mobject = SucInfo.objects.filter(id=mid)
    res = '无'
    if fobject[0].family != mobject[0].family:
        return {'pleafcolor': res, 'pleafopex_color': res, 'pplantshape': res, 'pleafshape': res, 'pleafopex': res}
    fleafcolor = fobject[0].leafcolor
    mleafcolor = mobject[0].leafcolor
    fleafopex_color = fobject[0].leafopex_color
    mleafopex_color = mobject[0].leafopex_color
    fplantshape = fobject[0].plantshape
    mplantshape = mobject[0].plantshape
    fleafshape = fobject[0].leafshape
    mleafshape = mobject[0].leafshape
    fleafopex = fobject[0].leafopex
    mleafopex = mobject[0].leafopex

    lccount = Hybridize.objects.filter(femaleparent__leafcolor=fleafcolor, maleparent__leafcolor=mleafcolor)
    count = 0
    pleafcolor = fleafcolor
    for x in lccount:
        cur = lccount.filter(progeny__leafcolor=x.progeny.leafcolor).count()
        if cur > count:
            count = cur
            pleafcolor = x.progeny.leafcolor

    loccount = Hybridize.objects.filter(femaleparent__leafopex_color=fleafopex_color,
                                        maleparent__leafopex_color=mleafopex_color)
    count = 0
    pleafopex_color = fleafopex_color
    for x in loccount:
        cur = loccount.filter(progeny__leafopex_color=x.progeny.leafopex_color).count()
        if cur > count:
            count = cur
            pleafopex_color = x.progeny.leafopex_color

    lscount = Hybridize.objects.filter(femaleparent__plantshape=fplantshape, maleparent__plantshape=mplantshape)
    count = 0
    pplantshape = fplantshape
    for x in lscount:
        cur = lscount.filter(progeny__plantshape=x.progeny.plantshape).count()
        if cur > count:
            count = cur
            pplantshape = x.progeny.plantshape

    lfcount = Hybridize.objects.filter(femaleparent__leafshape=fleafshape, maleparent__leafshape=mleafshape)
    count = 0
    pleafshape = fleafshape
    for x in lfcount:
        cur = lfcount.filter(progeny__leafshape=x.progeny.leafshape).count()
        if cur > count:
            count = cur
            pleafshape = x.progeny.leafshape

    locount = Hybridize.objects.filter(femaleparent__leafopex=fleafopex, maleparent__leafopex=mleafopex)
    count = 0
    pleafopex = fleafopex
    for x in locount:
        cur = locount.filter(progeny__leafopex=x.progeny.leafopex).count()
        if cur > count:
            count = cur
            pleafopex = x.progeny.leafopex
    return {'pleafcolor': pleafcolor, 'pleafopex_color': pleafopex_color, 'pplantshape': pplantshape, 'pleafshape': pleafshape, 'pleafopex': pleafopex}

def hybridization(requset):
    suclist = SucInfo.objects.all()
    return render(requset, 'hybapphtml/hybridization.html', {'suclist': suclist})

def hybresult(request):
    post = request.POST
    fid = post.get('femaleparent')
    mid = post.get('maleparent')
    fobject = SucInfo.objects.filter(id=fid)[0]
    mobject = SucInfo.objects.filter(id=mid)[0]
    objectlist = forecast(fid, mid)
    return render(request, 'hybapphtml/hybresult.html', {'fobject': fobject, 'mobject': mobject, 'resultdic': objectlist})

def hybinfolist(request, pageindex=1):
    hyblist = Hybridize.objects.all().order_by("id")
    p = Paginator(hyblist, 8)
    totalpages = p.num_pages
    pageindex = int(pageindex)
    hybpage = p.page(pageindex)
    pageindexlist = p.page_range
    return render(request, 'hybapphtml/hybinfolist.html', {'hybpage': hybpage, 'pageindexlist': pageindexlist, 'currentpage': pageindex, 'totalpages': totalpages})

def hybinfo(request, id):
    hybinfo = Hybridize.objects.filter(id=id)
    return render(request, 'hybapphtml/hybinfo.html', {'hybinfo': hybinfo})

def hybrecord(request):
    return render(request, 'hybapphtml/hybrecord.html')