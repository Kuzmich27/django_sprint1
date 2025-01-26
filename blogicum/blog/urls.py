from django.urls import path

from blog import views as blog_views


app_name = 'blog'


urlpatterns = [
    path('', blog_views.index, name='index'),
    path('posts/<int:id>/', blog_views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', blog_views.category_post,
         name='category_posts'),
    path('blog/not-my-day/', blog_views.not_my_day_blog, name='not_my_day'),
]
