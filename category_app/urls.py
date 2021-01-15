from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_category, name='view_category'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_sub_category/', views.create_sub_category, name='create_sub_category'),
    path('upload_excel/', views.insert_excel, name='upload_excel')
]
