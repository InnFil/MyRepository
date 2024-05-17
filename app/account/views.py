from random import randint

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response

from account.constants import CODE_LIFETIME
from account.models import LoginCode


class AccountAPI(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        if phone_number is None or str(phone_number).isdigit() is False:
            raise AuthenticationFailed("Номер телефона не был введен или ошибка в номера телефона")

        code = randint(1000, 9999)
        LoginCode.objects.create(phone_number=phone_number, code=code)
        # здесь нужно отправить код на телефон
        return Response({'status': 'ok'})


class AuthorizationCodeAPI(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        code = request.data.get("code")
        try:
            login_code = LoginCode.objects.get(phone_number=phone_number, code=code)
        except ObjectDoesNotExist:
            raise AuthenticationFailed("Неверный код авторизации")

        expiration_at = login_code.create_at + timezone.timedelta(minutes=CODE_LIFETIME)
        if expiration_at < timezone.now():
            raise AuthenticationFailed("Истек срок действия кода")
        return Response({'status': 'ok'})
