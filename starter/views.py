# -*- coding: utf-8 -*-
from __future__ import division, absolute_import

import json

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.traversal import resource_path
from pyramid.url import resource_url
from .resources import OrderCollection, Order, OrderConfirmation
from pyramid.security import remember
from pyramid.httpexceptions import HTTPMethodNotAllowed, HTTPUnsupportedMediaType, HTTPFound, HTTPSeeOther, HTTPNotImplemented

from starter.bl.service.repairorder import RepairOrder

def is_delete(info, request):
    return (request.method == 'DELETE' or
            request.POST.get('_method') == 'DELETE')

def is_put(info, request):
    return (request.method == 'PUT' or
            request.POST.get('_method') == 'PUT')


class BaseResource(object):
    """docstring for BaseResource"""
    def __init__(self, request):
        super(BaseResource, self).__init__()
        self.request = request

    def get_parent_url(self):
        uri = '/'.join(self.request.resource_url(self.request.context).split('/')[:-2])
        return uri


class OrderCollectionResource(BaseResource):
    """docstring for OrderCollectionResource"""

    @view_config(context=OrderCollection, request_method="HEAD")
    def head(self):
        raise HTTPNotImplemented

    @view_config(context=OrderCollection, request_method="GET")
    def get(self):
        """Return list of orders.
        Also mimics authorization for test purpose"""
        z = remember(self.request, 'nilcolor')
        result = json.dumps(RepairOrder().getListOfRepairOrders())
        return Response(result, headers=z)

    @view_config(context=OrderCollection, request_method="POST")
    def post(self):
        """Creates new order (in collection) and returns 301 code with its URI"""
        ro = RepairOrder()
        data = None
        try:
            data = {
                "id": self.request.POST["order_id"],
                "client": self.request.POST["client_id"],
                "number": self.request.POST["order_number"],
            }
        except Exception:
            raise HTTPUnsupportedMediaType
        order = ro.createNewRepairOrder(data)
        uri = self.request.resource_url(self.request.context, *(order["id"],))
        # return Response(json.dumps(order))
        # return Response(uri)
        return HTTPFound(location=uri)

    @view_config(context=OrderCollection, custom_predicates=(is_put,))
    def put(self):
        """Unused, not applicable"""
        raise HTTPMethodNotAllowed

    @view_config(context=OrderCollection, custom_predicates=(is_delete,))
    def delete(self):
        """Unused, not applicable"""
        raise HTTPMethodNotAllowed

class OrderResource(BaseResource):
    """docstring for OrderResource"""

    @view_config(context=Order, request_method="GET")
    def get(self):
        """Get concrete order
            Kind fo default view for /orders/{id} urls"""
        ro = RepairOrder()
        order = ro.getRepairOrderForID(long(self.request.context.__name__))
        order = json.dumps(order)
        return Response(order)

    @view_config(context=Order, request_method="POST")
    def post(self):
        """New Order should be created vie POST'ing to the Collection RC"""
        raise HTTPMethodNotAllowed

    @view_config(context=Order, custom_predicates=(is_put,))
    def put(self):
        """Update order with received data"""
        print self.request.POST # yeah... that strange, POST...

    @view_config(context=Order, custom_predicates=(is_delete,))
    def delete(self):
        """Delete order"""
        order_id = long(self.request.context.__name__)
        ro = RepairOrder()
        try:
            # there is no delete method there yet...
            # ro.deleteRepairOrder(order_id)
            pass
        except Exception:
            pass
        # remove last part of the URI (it must be ID and redirect there)
        raise HTTPSeeOther(self.get_parent_url()) # HTTP 303 - SeeOther. Should convert request to GET (versus DELETE!)


class OrderConfirmationResource(BaseResource):
    """docstring for OrderConfirmationResource"""

    @view_config(context=OrderConfirmation, request_method="GET")
    def get(self):
        """Get order confirmation?! Ha!"""
        raise HTTPMethodNotAllowed

    @view_config(context=OrderConfirmation, request_method="POST")
    def post(self):
        """Confirm order"""
        raise HTTPSeeOther(self.get_parent_url())

    @view_config(context=OrderConfirmation, custom_predicates=(is_put,))
    def put(self):
        """Create new order confirmation is a strange thus not allowed"""
        raise HTTPMethodNotAllowed

    @view_config(context=OrderConfirmation, custom_predicates=(is_delete,))
    def delete(self):
        """Delete order confirmation, i.e. un-confirm order.
        Good idea but not implemented yet"""
        raise HTTPNotImplemented


# class CustomerCollectionResource(BaseResource):
#     """docstring for CustomerCollectionResource"""

#     @view_config(context=, request_method=|custom_predicates=)
#     def get(self):
#         """Get something"""
#         raise HTTPNotImplemented

#     @view_config(context=, request_method=|custom_predicates=)
#     def post(self):
#         """Get something"""
#         raise HTTPNotImplemented

#     @view_config(context=, request_method=|custom_predicates=)
#     def put(self):
#         """Get something"""
#         raise HTTPNotImplemented

#     @view_config(context=, request_method=|custom_predicates=)
#     def delete(self):
#         """Get something"""
#         raise HTTPNotImplemented


# class CustomerResource(BaseResource):
#     """docstring for CustomerResource"""

#     @view_config(context=, request_method=|custom_predicates=)
#     def get(self):
#         """Get something"""
#         raise HTTPNotImplemented

#     @view_config(context=, request_method=|custom_predicates=)
#     def post(self):
#         """Get something"""
#         raise HTTPNotImplemented

#     @view_config(context=, request_method=|custom_predicates=)
#     def put(self):
#         """Get something"""
#         raise HTTPNotImplemented

#     @view_config(context=, request_method=|custom_predicates=)
#     def delete(self):
#         """Get something"""
#         raise HTTPNotImplemented


################################################################################


class OrderController(object):
    """docstring for Order"""
    def __init__(self, request):
        super(OrderController, self).__init__()
        self.request = request

    # View callable for order's client data: /orders/{id}/client
    @view_config(name='client', context=Order, request_method='GET')
    def get_order_client(self):
        ro = RepairOrder()
        order_id = long(self.request.context.__name__)
        client_id = ro.getRepairOrderForID(order_id)['client']
        result = "Here you are -  client for order '%s' is %s" % (order_id, client_id)
        return Response(result)


def my_view(request):
    return {'project':'Starter 0.0'}
