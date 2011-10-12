################################################################################
# Next code goes to views modules
################################################################################
from pyramid.response import Response
from pyramid.view import view_config
from resources import Bar

class FuckyView(object):
    def __init__(self, request):
        self.request = request

    @view_config(context=Bar)
    def fucky(request):
        return Response('fucky view')

class FuckyViewSecond(object):
    def __init__(self, request):
        self.request = request

    @view_config(context="starter.resources.Bar", request_method='POST')
    def fucky(request):
        return Response('fucky view second', )

def my_view(request):
    return {'project':'Starter 0.0'}
