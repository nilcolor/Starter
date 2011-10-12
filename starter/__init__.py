# -*- coding: utf-8 -*-
from __future__ import division, absolute_import

from pyramid.config import Configurator
from starter.resources import root_factory

from pyramid.events import subscriber
from pyramid.events import NewRequest

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(root_factory=root_factory, settings=settings)
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
