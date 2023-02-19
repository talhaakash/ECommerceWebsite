
from django.urls import path

from . import views

urlpatterns = [
    path("",  views.index, name = 'ShopHome'),
    path("about/",  views.about, name = 'AbouUS'),
    path("contact/",  views.contact, name = 'ContactUS'),
    path("tracker/",  views.tracker, name = 'TrackingStatus'),
    path("search",  views.search, name = 'Search'),
    path("productview",  views.prodview, name = 'Productview'),
    path("checkout",  views.checkout, name = 'CheckOut'),
    
]
