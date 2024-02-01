
from django.utils import timezone
from django.conf import settings
from visitor.models import Session

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user has a session key
        if not request.session.session_key:
            request.session.create()

        session_key = request.session.session_key

        # Check if a log entry already exists for the current session
        existing_log = Session.objects.filter(session_key=session_key).exists()

        if not existing_log:
            # Log visitor information
            ip_address = self.get_client_ip(request)
            Session.objects.create(
                session_key = session_key,
                ip = ip_address,
                timestamp=timezone.now()
            )

            # Send the session key to the client as a cookie
            response = self.get_response(request)
            response.set_cookie('session_key', session_key, max_age=settings.SESSION_COOKIE_AGE)
        else:
            response = self.get_response(request)
        print(session_key)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip