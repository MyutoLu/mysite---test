from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.practice,name='practice'),
    #path('<year>/<int:month>/<slug:day>',views.mydate, name='mydate'),
    re_path('(?P<year>[0-9]{4})',views.myyear, name='myyear'),
]
