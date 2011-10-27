# -*- coding: utf-8 -*-
from __future__ import division, absolute_import

from pyramid.config import Configurator
from starter.resources import AppRoot
from starter.auth import FakeAuthorizationPolicy
# from starter.auth import FakeAuthorizationPolicy
from pyramid.authentication import AuthTktAuthenticationPolicy

from pyramid.events import subscriber
from pyramid.events import NewRequest, ContextFound
from pyramid.httpexceptions import HTTPUnauthorized, HTTPForbidden

# TODO: take a look at http://docs.pylonsproject.org/projects/pyramid/1.2/narr/hooks.html
# lots of cool stuff to use here

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    authentication_policy = AuthTktAuthenticationPolicy('secretkey123456')
    authorization_policy = FakeAuthorizationPolicy()

    config = Configurator(
        root_factory=AppRoot,
        settings=settings,
        authentication_policy=authentication_policy,
        authorization_policy=authorization_policy
    )
    config.set_default_permission('view')
    # To configure the slash-appending not found view in your application, change the application’s startup configuration, adding the following stanza
    # config.add_view(context='pyramid.exceptions.NotFound', view='pyramid.view.append_slash_notfound_view')
    # config.add_view('starter.views.my_view',
    #                 context='starter:resources.Root',
    #                 renderer='starter:templates/mytemplate.pt')
    config.add_static_view('static', 'starter:static', cache_max_age=3600)

    # Configurator.scan() should be called to activate subscribers... and @view_configs
    config.scan()

    return config.make_wsgi_app()


def cleanup_callback(request):
    # here we can clean-up their request
    # ie commit/rollback DB session or log something...
    print("request clean-up action")
    pass

@subscriber(NewRequest)
def add_cleanup_callback(event):
    event.request.add_finished_callback(cleanup_callback)
    print "%s -> %s" % (event.request.method, event.request.url)

# will be called when context is found (in resource tree)
@subscriber(ContextFound)
def csrf_validation_event(event):
    request = event.request
    # user = getattr(request, 'user', None)
    # csrf = request.params.get('csrf_token')
    # if (request.method == 'POST' or request.is_xhr) and \
    #     (user and user.is_authenticated()) and \
    #     (csrf != unicode(request.session.get_csrf_token())):
    # # summary - you can check something and pass-through request or
    # # raise HTTP error here.

    if False and request.cookies.get('sid', None) != '1234567890':
        raise HTTPForbidden
