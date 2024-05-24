from django.urls import path,re_path
from .views import EmployeeView
 
urlpatterns = [
    path('employee/',EmployeeView.as_view(),name='employee'),
    path('employee/<int:id>',EmployeeView.as_view(),name='employee')

    #  re_path(r'^.*\.*', views.pages, name='pages'), 
]