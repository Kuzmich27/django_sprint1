from django.urls import path
from pages import views as pages_views


app_name = 'pages'


urlpatterns = [
    path('about/', pages_views.about, name='about'),
    path('rules/', pages_views.rules, name='rules'),
    path('pages/not_my_day/', pages_views.not_my_day, name='not_my_day')
]
