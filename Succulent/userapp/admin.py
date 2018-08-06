from django.contrib import admin
#zero zero110119
# Register your models here.
from userapp.models import *


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'uname', 'upwd', 'uemail']
    list_filter = ['uname']
    search_fields = ['uname']
    list_per_page = 8
    search_fields = ('title',)
    # fields = ['umane', 'upwd', 'uemail']
    fieldsets = [
        ('basic', {'fields': ['uname']}),
        ('more', {'fields': ['upwd', 'uemail']}),
    ]

admin.site.register(UserInfo, UserInfoAdmin)