from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.backends import ModelBackend

from account.models import User
from django.db.models import Q


class AuthBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username) | Q(phone=username))
        except ObjectDoesNotExist:
            return None

        if user.check_password(password):
            return user

        else:
            return None
