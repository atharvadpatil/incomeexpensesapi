from rest_framework import renderers
import json


class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': data}) #json.dumps() function converts a Python object into a json string.
        else:
            response = json.dumps({'data': data})
        return response