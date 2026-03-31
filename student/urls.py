from django.urls import path
from .views import home , student , student_add , student_info ,student_info_update,student_info_delete
urlpatterns = [
    path('',home,name='home'),
    path('student/',student,name='student'),
    path('students/',student_add,name='student_add'),
    path('students/<int:pk>',student_info,name='student_info'),
    path('students/<int:pk>update/',student_info_update,name='student_info_update'),
    path('students/<int:pk>/delete/',student_info_delete,name='student_info_delete'),
]