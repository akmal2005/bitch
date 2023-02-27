from django.contrib.sites import requests
from rest_framework.authtoken.models import Token

from account.models import User


def regis(self, params):
    user = User.objects.filter(username=data.params("username")).first()
    if user:
        return {
            "Error": "Bunaqa foydalanuvchi bor"
        }

    serilizer = self.get_serializer(data=params)
    serilizer.is_valid(raise_exception=True)
    root = serilizer.create(serilizer.data)
    root.set_password(data['password'])
    root.save()
    token = Token()
    token.user = root
    token.save()

    return {
        "token": token.key
    }