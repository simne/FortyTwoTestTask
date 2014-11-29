import json
from django.utils.html import escape

from hello.models import MHttpRequest

class StoreHttpReqs(object):

    def process_request(self, request):

        # META: 
        fields = [
            'CONTENT_LENGTH', 'CONTENT_TYPE', 'HTTP_ACCEPT_ENCODING',
            'HTTP_ACCEPT_LANGUAGE', 'HTTP_HOST',
            'HTTP_REFERER', 'HTTP_USER_AGENT','QUERY_STRING', 'REMOTE_ADDR',
            'REMOTE_HOST', 'REMOTE_USER', 'REQUEST_METHOD', 'SERVER_NAME',
            'SERVER_PORT'
        ]

        mm = MHttpRequest( meta_PATH_INFO = request.__dict__['META']['PATH_INFO'] )
        mm.get = getattr(request, 'GET')
        mm.post = getattr(request, 'POST')
        mm.cookies = getattr(request, 'COOKIES')
        mm.files = getattr(request, 'FILES')
        mm.meta_PATH_INFO = request.__dict__['META']['PATH_INFO']

        for kk in fields:
            if kk in request.__dict__['META'].keys():
                #print "%s%s" % ('meta_',kk)
                aaa = "%s%s" % ('meta_', kk)
                setattr( mm, aaa, request.__dict__['META'][kk] )

        # store request whole

        mm.rqdump = escape(repr(request))

        mm.save()

        return None
