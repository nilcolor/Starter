# -*- coding: utf-8 -*-
from __future__ import division, absolute_import

from pyramid.response import Response
from pyramid.view import view_config
from .resources import Bar

class FuckyView(object):
    def __init__(self, request):
        self.request = request

    @view_config(context=Bar)
    def default(self):
        return Response('default view called...')

    @view_config(context=Bar, request_method='GET')
    def fucky(self):
        return Response('GET:fucky view')

class FuckyViewSecond(object):
    def __init__(self, request):
        self.request = request

    @view_config(context="starter.resources.Bar", request_method='POST')
    def fucky(self):
        return Response('POST:fucky view second', status="201")

def my_view(request):
    return {'project':'Starter 0.0'}
