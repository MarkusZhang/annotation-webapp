from django.conf.urls import include, url
from django.contrib import admin
from webapp.views import home,submit_annotation, user_login, user_logout


urlpatterns = [
    # Examples:
    url(r'^$', user_login ),
    url(r'^logout$', user_logout ),
    # url(r'^blog/', include('blog.urls')),
    url(r'^survey$',home),
    url(r'^submit_annotation',submit_annotation),
    url(r'^admin/', include(admin.site.urls)),
]
