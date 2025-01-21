from django.urls import path

from pages import views as pages_views


app_name = 'pages'


urlpatterns = [
    path('about/', pages_views.about, name='about'),
    path('rules/', pages_views.rules, name='rules'),
]
