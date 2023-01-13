import synonyms
from goods.models import Goods
from django.contrib.auth.models import User


def fetch_all_offers(user:User):
    offers = Goods.objects.all().filter(user=user).filter(property_type=1)
    return list(offers)    

def fetch_all_needs():
    return list(Goods.objects.filter(property_type = 0))

def get_string_tag(offer_list):
    string_list = [i.name + i.category.name + i.goods_brief + i.goods_desc for i in offer_list]
    return ''.join(string_list)

# 需要验证string_tag != ''
def sort_by_similarity(needs_list:list, string_tag):
    needs_list.sort(key=lambda i: synonyms.compare(string_tag, i.name + i.category.name + i.goods_brief + i.goods_desc) if i else 0, reverse=True)
    return needs_list

