from django.contrib import admin
from django.conf.urls import patterns, url, include
admin.autodiscover()

from usergroups import options

from example.groups.models import Group


urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('usergroups.urls')),
    
)


class GroupConfig(options.BaseUserGroupConfiguration):
    pass

options.register('test', Group, GroupConfig)