from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import manage_items, UserViews, UserDetail



urlpatterns = {
    re_path(r'^$', UserViews.as_view(), name='index'),
    path('api/redis', manage_items, name="items redis"),
    path('api/users', UserViews.as_view(), name="users"),
    path('api/users/<int:pk>', UserDetail.as_view()),
}
urlpatterns = format_suffix_patterns(urlpatterns)
