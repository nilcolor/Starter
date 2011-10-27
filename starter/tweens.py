# -*- coding: utf-8 -*-

def method_printing_tween_factory(handler, registry):
    def method_printing_tween(request):
        print request
        try:
            # i HAVE to process raise HTTP* here... or it fails
            response = handler(request)
        finally:
            pass

        return response

    return method_printing_tween
