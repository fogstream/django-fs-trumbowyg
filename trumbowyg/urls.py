# coding=utf-8

from django.conf.urls import url, patterns

from trumbowyg.views import upload_image


urlpatterns = patterns('',
    url('^upload_image/$', upload_image, name='trumbowyg_upload_image'),
)
