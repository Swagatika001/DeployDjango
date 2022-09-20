
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/book/',include('bookstore.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/certificates/', include('certificates.urls')),
    path('api/v1/lectures/', include('lecturers.urls')),
]
