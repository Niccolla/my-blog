from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^$', views.post_list, name='post_list'),
]
