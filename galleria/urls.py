from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.day_today,name='Today'),
    url(r'^categories/(\d{4}-\d{2}-\d{2})/$',views.photo_category,name = 'category')
    url(r'^search/', views.search_results, name='search_results')
]