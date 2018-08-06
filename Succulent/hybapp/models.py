from django.db import models
from sucapp.models import SucInfo


# Create your models here.

class Hybridize(models.Model):
    maleparent = models.ForeignKey(SucInfo, related_name='male', on_delete=models.CASCADE)
    femaleparent = models.ForeignKey(SucInfo, related_name='female', on_delete=models.CASCADE)
    progeny = models.ForeignKey(SucInfo, related_name='progeny', on_delete=models.CASCADE)

    # filter_horizontal = ('maleparent', 'femaleparent', 'progeny')

    def __str__(self):
        return '%s x %s' % (self.femaleparent.name, self.maleparent.name)

    class Meta:
        unique_together = ("maleparent", "femaleparent")
        verbose_name = '杂交数据'
        verbose_name_plural = '杂交数据'
