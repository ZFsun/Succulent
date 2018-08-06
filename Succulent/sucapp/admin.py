from django.contrib import admin
from sucapp.models import *

# Register your models here.

# admin.site.register(SucInfo)
# admin.site.register(Maintain)
@admin.register(SucInfo)
class SucInfoAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'family', 'genus')
    list_per_page = 15
    ordering = ('id',)
    # list_editable = ['name', 'family', 'genus']
    # fk_fields = ('family',)
    list_display_links = ('id', 'name')
    list_filter = ('family', 'genus')
    search_fields = ('name',)
    fieldsets = [
        ('基础信息', {'fields': ['image', 'name', 'family', 'genus']}),
        ('性状信息', {'fields': ['plantshape', 'leafcolor', 'leafshape', 'leafopex_color', 'leafopex']}),
        ('养护信息', {'fields': ['lighttime', 'water', 'temperature', 'season', 'introduction']}),
        ('亲本信息', {'fields': ['maleparent', 'femaleparent']}),
    ]

admin.site.site_header = '多肉植物品种记录及杂交新品性状预测及记录系统'
admin.site.site_title = '多肉植物杂交预测后台管理'


@admin.register(Maintain)
class MainAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'editDate', 'author')
    date_hierarchy = 'editDate'
    search_fields = ('title',)
    list_display_links = ('id', 'title')
    fieldsets = [
        ('作者', {'fields': ['author', 'editDate']}),
        ('文章', {'fields': ['title', 'content']}),
    ]

@admin.register(FamilyGenus)
class FamilyGenusAdmin(admin.ModelAdmin):
    list_display=('id', 'family', 'genus')
