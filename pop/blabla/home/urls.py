from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='homepage'),
    path('other/',other,name='otherpage'),
    path('other1/',other1,name='otherpage1'),
    path('other2/',other2,name='otherpage2'),
    ]
