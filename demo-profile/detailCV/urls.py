from django.urls import path
from . import views
app_name= 'detail'
urlpatterns=[
    path('index/',views.IndexClass.as_view(),name='index'),
]