from django.urls import path, re_path
from .views import  (news_today, past_days_news, search,
     article, new_article, logout_view, profile, update_profile )


urlpatterns = [
    path('', news_today, name='todat_news'),
    re_path(r'archives/(\d{4}-\d{2}-\d{2})/', past_days_news, name='pastnews'),
    path('search/', search, name='search'),
    re_path(r'article/(\d+)', article, name ='article'),
    path('new/article/', new_article, name='new_article' ),
    path('logouts/', logout_view, name='logouts'),
    path('update_profile/', update_profile, name='update_profile'),
    path('profile/', profile, name='profile'),
]