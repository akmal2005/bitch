from collections import OrderedDict

from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from API.v1.auth.services import regis
from account.models import User
from .serializer import UserSerializer





class AuthView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, requests, *args, **kwargs):
        data = requests.data
        method = data.get("method")
        params = data.get("params")
        if not method:
            return Response({
                "Error": "method kiritlishi kerak"
            })
        if params is None:
            return Response({
                "Error": "params kiritlishi kerak"
            })

        if method == "regis":
            return Response(regis(self, params))

class RegisView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, requests, *args, **kwargs):
        data = requests.data
        user = User.objects.filter(username=data.get("username")).first()
        if user:
            return Response({
                "Error": "Bunaqa foydalanuvchi bor"
            })

        serilizer = self.get_serializer(data=data)
        serilizer.is_valid(raise_exception=True)
        root = serilizer.create(serilizer.data)
        root.set_password(data['password'])
        root.save()
        token = Token()
        token.user = root
        token.save()

        return Response({
            "token": token.key
        })


class LoginView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        if "username" not in data or "password" not in data:
            return Response({
                "Error": "Kerakli narsalar kiritilmagan"
            })


        user = User.objects.filter(username= data['username']).first()
        if not user:
            return Response({
                "Error": "User topilmadi"
            })
        if not user.check_password(data['password']):
            return Response({
                "Error": "Parol xato "
            })


        token = Token.objects.get_or_create(user= user)
        print(token)
        return Response({
            "token": token[0].key
        })


def format_user(data):
    return OrderedDict([
        ("id", data.id),
        ("first_name", data.first_name),
        ("last_name", data.last_name),
        ("username", data.username),
        ("phone", data.phone),
        ("password", data.password)

    ])



class UserActionsView(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = UserSerializer


    def get(self,requests):
        ser = self.get_serializer(data = {}, instance = requests.user)
        ser.is_valid()

        return Response({
            "user": ser.data
        })




    def post(self, requests):
        data = requests.data
        if "old" not in data or "new" not in data:
            return Response({
                "Error": "data to`liq emas"
            })

        if not requests.user.check_password(data['old']):
            return Response({
                "Error": "parol xato"
            })

        requests.user.set_password(data['new'])
        requests.user.save()



        return Response({
            "Success": "parol o`zgartirildi"
        })























