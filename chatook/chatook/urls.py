# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views import defaults as default_views

from usuarios.views import UsersListView, UserDetailView
from chat.views import  newMessageView, chatListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', UsersListView.as_view(), name="home"),
    url(r'^usuario/(?P<pk>[0-9]+)/$', UserDetailView.as_view(),
        name='user_detail'),
    url(r'^new_message/(?P<pk>[0-9]+)$', newMessageView, name="new_message"),
    url(r'^chat/(?P<pk>[0-9]+)/with/(?P<pk2>[0-9]+)$', chatListView, name="chat"),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.

    urlpatterns += [
        url(r'^400/$', default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
