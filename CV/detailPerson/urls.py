from django.urls import path
from . import views
app_name='detailPerson'
urlpatterns=[
    path('contact/',views.Contact.as_view(),name='contact'),
]