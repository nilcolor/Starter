# -*- coding: utf-8 -*-
# Auth stub module
from pyramid.traversal import resource_path
from pyramid.security import *

class FakeAuthenticationPolicy(object):
    """ An object representing a Pyramid authentication policy. """

    def authenticated_userid(self, request):
        """ Return the authenticated userid or ``None`` if no
        authenticated userid can be found. This method of the policy
        should ensure that a record exists in whatever persistent store is
        used related to the user (the user should not have been deleted);
        if a record associated with the current id does not exist in a
        persistent store, it should return ``None``."""
        print "authenticated_userid:: request: %s" % request
        return "ablinov"

    def unauthenticated_userid(self, request):
        """ Return the *unauthenticated* userid.  This method performs the
        same duty as ``authenticated_userid`` but is permitted to return the
        userid based only on data present in the request; it needn't (and
        shouldn't) check any persistent store to ensure that the user record
        related to the request userid exists."""
        print "unauthenticated_userid:: request: %s" % request
        return "ablinov"

    def effective_principals(self, request):
        """ Return a sequence representing the effective principals
        including the userid and any groups belonged to by the current
        user, including 'system' groups such as
        ``pyramid.security.Everyone`` and
        ``pyramid.security.Authenticated``. """
        print "effective_principals::"
        return "ablinov"

    def remember(self, request, principal, **kw):
        """ Return a set of headers suitable for 'remembering' the
        principal named ``principal`` when set in a response.  An
        individual authentication policy and its consumers can decide
        on the composition and meaning of **kw. """
        print "remember::"
        return "X-FAKE_USER"

    def forget(self, request):
        """ Return a set of headers suitable for 'forgetting' the
        current user on subsequent requests. """
        print "forget::"
        return "X-FAKE_USER"


class FakeAuthorizationPolicy(object):
    """ An object representing a Pyramid authorization policy. """
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
