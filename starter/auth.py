# -*- coding: utf-8 -*-
# Auth stub module
from pyramid.traversal import resource_path
from zope.interface import implements
from pyramid.interfaces import IAuthorizationPolicy
from pyramid.security import *

class FakeAuthorizationPolicy(object):
    """ An object representing a Pyramid authorization policy. """
    implements(IAuthorizationPolicy)

    def permits(self, context, principals, permission):
        """ Return ``True`` if any of the ``principals`` is allowed the
        ``permission`` in the current ``context``, else return ``False``
        """
        print "permits:: %s => %s for %s" % (permission, resource_path(context), authenticated_userid(context.request))
        return True

    def principals_allowed_by_permission(self, context, permission):
        """ Return a set of principal identifiers allowed by the
        ``permission`` in ``context``.  This behavior is optional; if you
        choose to not implement it you should define this method as
        something which raises a ``NotImplementedError``.  This method
        will only be called when the
        ``pyramid.security.principals_allowed_by_permission`` API is
        used."""
        print "principals_allowed_by_permission::"
        raise NotImplementedError
