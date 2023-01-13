from haystack import indexes
from goods.models import Goods


class NeedsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr="name")
    goods_brief = indexes.CharField(model_attr="goods_brief")
    goods_desc = indexes.CharField(model_attr="goods_desc")
    goods_sn = indexes.IntegerField(model_attr="goods_sn")
    autocomplete = indexes.EdgeNgramField()
    def get_model(self):
        return Goods

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(property_type=0)