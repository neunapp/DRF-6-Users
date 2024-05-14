
from django.utils import timezone

from rest_framework.authtoken.models import Token


class TokenExpiredMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print('--- mi middleware ---')
        # eliminar tokens expirados
        Token.objects.filter(
            user__token_expired__lt=timezone.now()
        ).delete()
        
        response = self.get_response(request)
        return response