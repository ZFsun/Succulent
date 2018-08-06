from django.db import models
import django.utils.timezone as timezone
from tinymce.models import HTMLField
# Create your models here.
class SucInfo(models.Model):
    image = models.ImageField('图片', upload_to='sucapp/')
    name = models.CharField('名称', max_length=20)
    family = models.CharField('科', max_length=20)
    genus = models.CharField('属', max_length=20)
    plantshape = models.CharField('植株形状', max_length=8)
    leafcolor = models.CharField('叶子颜色', max_length=8)
    leafshape = models.CharField('叶子形状', max_length=10)
    leafopex_color = models.CharField('叶尖颜色', max_length=4)
    leafopex = models.CharField('叶尖长度', max_length=4)
    lighttime = models.IntegerField('光照时间', )
    water = models.CharField('水分', max_length=20)
    temperature = models.CharField('温度', max_length=16)
    season = models.CharField('季节', max_length=8)
    introduction = models.TextField('简介', max_length=1000)
    maleparent = models.ForeignKey('self', related_name='sucmale', on_delete=models.CASCADE, blank=True, null=True)
    femaleparent = models.ForeignKey('self', related_name='sucfemale', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '多肉数据'
        verbose_name_plural = '多肉数据'


class Maintain(models.Model):
    title = models.CharField('标题', max_length=30)
    editDate = models.DateTimeField('保存日期',default = timezone.now)
    author = models.CharField('作者', max_length=8)
    content = HTMLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '养护知识'
        verbose_name_plural = '养护知识'


class FamilyGenus(models.Model):
    family = models.CharField(max_length=20)
    genus = models.CharField(max_length=20)

    def __str__(self):
        return '%s/%s'%(self.family, self.genus)

    class Meta:
        verbose_name = '科属表'
        verbose_name_plural = '科属表'
