from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls', namespace='pages')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('blog.urls', namespace='blog_root')),
]
