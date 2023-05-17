from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User


class SignIn(APIView):

    def get(self, request):
        return render(request, 'account/signIn.html')

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email is None:
            return Response(status=400, data=dict(message='이메일을 입력해주세요'))

        if password is None:
            return Response(status=400, data=dict(message='비밀번호를 입력해주세요'))

        user = User.objects.filter(email=email).first()

        if user is None or check_password(password, user.password) is False:
            return Response(status=400, data=dict(message='아이디 또는 비밀번호가 잘못되었습니다'))

        request.session['signInCheck'] = True
        request.session['email'] = user.email

        return Response(status=200, data=dict(message='로그인에 성공했습니다'))


class SignUp(APIView):

    def get(self, request):
        return render(request, 'account/signUp.html')

    def post(self, request):
        password = request.data.get('password')
        email = request.data.get('email')
        nickname = request.data.get('nickname')
        name = request.data.get('name')

        if User.objects.filter(email=email).exists():
            return Response(status=400, data=dict(message='해당 이메일 주소가 존재합니다'))
        elif User.objects.filter(nickname=nickname).exists():
            return Response(status=400, data=dict(message="닉네임 '" +nickname+ "'이(가) 존재합니다"))

        User.objects.create(password=make_password(password),
                            email=email,
                            nickname=nickname,
                            name=name)

        return Response(status=200, data=dict(message='회원가입이 완료되었습니다. 로그인을 해주세요'))