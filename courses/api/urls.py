from django.urls import path, include
from rest_framework import routers
from .views import *


app_name = 'courses_api'

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    # path('courses/<int:pk>/enroll/', CourseEnrollView.as_view(), name='course_enroll'),
    path('', include(router.urls))
]
