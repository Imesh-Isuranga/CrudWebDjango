from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts,name="posts"),
    path('singlepost/<str:pid>/', views.post,name="post"),
    path('create-form', views.createNewpost,name="create"),
    path('update-form/<str:pid>/', views.updatepost,name="update"),
    path('delete/<str:pid>/', views.delete,name="delete"),
]