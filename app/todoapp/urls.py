from django.urls import path
from .views import Views
from django.conf import settings


urlpatterns = [
    path('get/', Views.getData),
    path('post/', Views.postData),
    path('put/<int:pk>/', Views.putData),
    path('delete/<int:pk>/', Views.deleteData),
    path('search/', Views.searchData)
]
