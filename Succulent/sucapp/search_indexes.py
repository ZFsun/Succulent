from haystack import indexes
from .models import *


class MaintainIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Maintain

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class SucInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return SucInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()