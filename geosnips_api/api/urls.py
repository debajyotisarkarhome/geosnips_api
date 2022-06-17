from django.urls import path
from .views import Create,Read,Update,Delete
urlpatterns = [
    path('api/read', Read),
    path('api/create', Create),
    path('api/update', Update),
    path('api/delete', Delete),
]
