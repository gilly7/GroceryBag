from django.urls import path

from bag.views import add_item, index

urlpatterns = [
    path('', index, name='index'),
    path('add-item', add_item, name='add-item'),
]