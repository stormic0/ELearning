from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from courses.views import CourseListView
from django.urls import path, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('course/', include('courses.urls', namespace='courses')),
    path('students/', include('students.urls', namespace='students')),
    path('api/', include('courses.api.urls', namespace='courses_api')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('', CourseListView.as_view(), name='course_list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
