What da-hell is this?
=====================

This is my [Pyramid][pyramid] playground.  
Here I make some expiriments with Pyramid. Learn how thing are build. How to live
with [traversal][1]. How to use MongoDB here and how to craft JSON response here...
So -- it _is_ playground.  
You can read it ofcourse, if you wish...

What's here right now?
----------------------

- Very simple resource tree (check resources.py).
- More than useless two view callables which responds to `GET:/foo/bar` and `POST:/foo/bar`
- DB shim used to simulate DB work
- Base security class. It allows everything but it's for now ;)
- Experiments with resource/subresource scheme

Thats all for now. Infant, yeah...

What's next?
------------

- Security based on resource tree (resource access list/permissions)
- some real DB works
- Row-level security (view-based)




[pyramid]: https://www.pylonsproject.org/
[1]: https://docs.pylonsproject.org/projects/pyramid/1.0/narr/traversal.html
[akhet]: http://pyramid.chromaticleaves.com/simpleauth/
