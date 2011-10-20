# -*- coding: utf-8 -*-
from __future__ import division, absolute_import

import json

from pyramid.response import Response
from pyramid.view import view_config
# from .resources import Bar
from .resources import OrderCollection, Order
from pyramid.security import remember
from pyramid.httpexceptions import HTTPMethodNotAllowed

from .db_shim import OrderModel

def is_delete(info, request):
    return (request.method == 'DELETE' or
            request.POST.get('_method') == 'DELETE')


class OrderController(object):
    """docstring for Order"""
    def __init__(self, request):
        super(OrderController, self).__init__()
        self.request = request

    # View to be used to get list of orders
    @view_config(context=OrderCollection, request_method='GET')
    def orders_list(self):
        z = remember(self.request, 'nilcolor')
        result = json.dumps(OrderModel(None).all())
        return Response(result, headers=z)

    # Kind fo default view for /orders/{id} urls
    @view_config(context=Order, request_method='GET')
    def single_order(self):
        model = OrderModel(None)
        order = model.one(long(self.request.context.__name__))
        order = json.dumps(order)
        return Response(order)

    # View callable for order's client data: /orders/{id}/client
    @view_config(name='client', context=Order, request_method='GET')
    def get_order_client(self):
        model = OrderModel(None)
        order_id = long(self.request.context.__name__)
        client_id = model.one(order_id)['client']
        result = "Here you are -  client for order '%s' is %s" % (order_id, client_id)
        return Response(result)

    # DELETE order responder - not allowed
    @view_config(context=Order, custom_predicates=(is_delete,))
    def remove_order(self):
        raise HTTPMethodNotAllowed


def my_view(request):
    return {'project':'Starter 0.0'}
