from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Hybridize)
class HybridizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'femaleparent', 'maleparent', 'progeny')
    list_per_page = 15
    ordering = ('id',)
    # fk_fields = ('femaleparent',)
    list_display_links = ('id', )
    # list_filter = ('femaleparent', 'maleparent')
    search_fields = ('femaleparent', 'maleparent', 'progeny',)
    # raw_id_fields = ('femaleparent')
