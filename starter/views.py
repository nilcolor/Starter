# -*- coding: utf-8 -*-
from __future__ import division, absolute_import

from pyramid.response import Response
from pyramid.view import view_config
from .resources import Bar
from pyramid.security import remember

def is_delete(info, request):
    return (request.method == 'DELETE' or
            request.POST.get('_method') == 'DELETE')


class FuckyView(object):
    def __init__(self, request):
        self.request = request

    # Responds to ANY:/foo/bar URL (context == Bar)
    # GET and DELETE have special handlers
    @view_config(context=Bar, permission="list")
    def default(self):
        return Response('default view called...')

    # Responds to GET:/foo/bar URL (context == Bar)
    @view_config(context=Bar, request_method='GET')
    def fucky(self):
        return Response('GET:fucky view')

    # Responds to DELETE:/foo/bar URL (context == Bar)
    @view_config(context=Bar, custom_predicates=(is_delete,))
    def delete_something(self):
        print("OK. Something deleted.")
        return Response("OK. Something deleted")

class FuckyViewSecond(object):
    def __init__(self, request):
        self.request = request

    # Responds to POST:/foo/bar URL (context == Bar)
    @view_config(context="starter.resources.Bar", request_method='POST', permission="add")
    def fucky(self):
        z = remember(self.request, 'nilcolor')
        return Response('POST:fucky view second', status="201", headers=z)

    # Responds to ANY:/foo/bar/go URL (context == Go)
    @view_config(context="starter.resources.Go")
    def go(self):
        return Response('Go view')

def my_view(request):
    return {'project':'Starter 0.0'}
