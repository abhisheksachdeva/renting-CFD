from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from renting.models import MyUser
from renting.serializers import UserRegSerializer
from rest_framework import mixins
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework import filters


factory = APIRequestFactory()
request = factory.get('/')


serializer_context = {
    'request': Request(request),
}


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class RegUser(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserRegSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = self.create(request, *args, **kwargs)
        except:
            return Response({'detail': "Fill required details or Email id already registered."})
        return Response({'detail': "Successfully registered."})

    def get(self, request):
        return Response({'detail': "Get response"})


class Login(APIView):

    def post(self, request, *args, **kwargs):
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
        except:
            return Response({'detail': "Enter Email and Password"})

        try:
            user = authenticate(email=email, password=password)
            if not user:
                return Response({'detail': "Email or Password was incorrect"})
        except:
            return Response({'detail': "Email or Password was incorrect"})

        try:
            token = Token.objects.get(user=user)

        except:
            token = Token.objects.create(user=user)
        login(request, user)
        user.is_active = True
        user.save()
        user_seri = UserRegSerializer(instance=user, context=serializer_context)
        return Response({'userInfo': user_seri.data, 'token': token.key})

    def get(self, request):
        return Response({'detail': "login GET response"})


class TokenView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        return Response({'detail': str(user)})
