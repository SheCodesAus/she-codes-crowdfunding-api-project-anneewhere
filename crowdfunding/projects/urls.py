from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views 

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"), #a name for the url pattern is a standard in restframework
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project-detail"),
    path('pledges/', views.PledgeList.as_view(), name="pledge-list"),
]

urlpatterns = format_suffix_patterns(urlpatterns) #format_suffix_patterns helps django format patterns properly?
