import synonyms
from RingoBackend.goods.models import Goods
from django.contrib.auth.models import User


def fetch_all_offers(user:User):
    offers = Goods.objects.all().filter(user=user).filter(property_type=1)
    return list(offers)    

