from django.test import TestCase
from .models import *

# Create your tests here.
def forecast(fid, mid):
    fobject = SucInfo.objects.filter(id=fid)
    mobject = SucInfo.objects.filter(id=mid)
    fleafopex = fobject[0].leafopex
    mleafopex = mobject[0].leafopex
    locount = Hybridize.objects.filter(femaleparent__leafopex=fleafopex, maleparent__leafopex=mleafopex)
    count = 0
    pleafopex = fleafopex
    for x in locount:
        cur = locount.filter(progeny__leafopex=x.progeny.leafopex).count()
        if cur > count:
            count = cur
            pleafopex = x.progeny.leafopex
    return pleafopex