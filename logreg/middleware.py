from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect

from logreg.models import User


class UserLoginMiddleware:

    @staticmethod
    def process_request(request):
        id = request.session.get("id", None)
        if id is None:
            request.user = AnonymousUser()
        else:
            try:
                request.user = User.objects.get(pk=int(id))
            except User.DoesNotExist:
                # if it's invalid, clear out their login
                del request.session["id"]
                return HttpResponseRedirect("/login/")