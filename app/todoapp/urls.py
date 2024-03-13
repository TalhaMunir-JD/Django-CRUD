from django.urls import path
from .views import getData, postData, putData, deleteData, searchData
from django.conf import settings


urlpatterns = [
    path('get/', getData),
    path('post/', postData),
    path('put/<int:pk>/', putData),
    path('delete/<int:pk>/', deleteData),
    path('search/', searchData)
]
