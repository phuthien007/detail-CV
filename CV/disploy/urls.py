from django.urls import path
from . import views

app_name = 'disploy'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('project/',views.ProjectClass.as_view(),name='project'),
]
