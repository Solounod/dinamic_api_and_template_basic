from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from apps.users.authentication import ExpiringTokenAuthentication

class Authentication(object):

    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
                
            except:
                return None
            
            token_expired = ExpiringTokenAuthentication()            
            user, token, message = token_expired.authenticate_credentials(token)
            if user != None and token != None:
                return user
            return message
                
        return None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        if user is not None:
            if type(user) == str:
                response =  Response({'error': user})
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                return response
            return super().dispatch(request, *args, **kwargs)
        response = Response ({'error': 'Credential not found'})
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response