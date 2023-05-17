from django.urls import path

from account.views import SignIn, SignUp

urlpatterns = [
    path('signIn', SignIn.as_view(), name='signIn'),
    path('signUp', SignUp.as_view(), name='signUp')
]