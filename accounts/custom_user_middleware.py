from django.contrib.auth.models import User
from django.http import HttpResponse

class SpecialUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.session.get('_auth_user_id')
        if user_id:
            user = User.objects.get(id=user_id)
            return HttpResponse(f"You are user {user}!")
        return self.get_response(request)

from django.urls import reverse, resolve
from django.http import HttpResponseRedirect

class ProtectSpecificRoutesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # List of protected URL names
        protected_url_names = [
            'home',
            'post_new',
            'post_edit',
            'post_delete',
        ]

        # Resolve the current path to its URL name
        try:
            current_url_name = resolve(request.path_info).url_name
        except:
            current_url_name = None

        # Check if the current URL name is in the protected list and the user is not authenticated
        if current_url_name in protected_url_names and not request.user.is_authenticated:
            # Redirect the user to the login page or any other page
            return HttpResponseRedirect(reverse('login'))

        response = self.get_response(request)
        return response

