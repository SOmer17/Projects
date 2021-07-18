from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.student_list,name="student_list"),
    path('view/<int:pk>',views.student_view,name="student_view"),
    path('edit/<int:pk>',views.update,name="student_edit"),
    path('delete/<int:pk>',views.delete,name="student_delete"),
    path('create/',views.create,name="student_create"),
]