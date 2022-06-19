import ssl
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_text
from rest_framework import status, permissions
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.encoding import force_bytes

from django.conf import settings
from .models import Account
from .serializers import AccountSerializer, AccountDetailsSerializer, ChangePasswordSerializer, UpdateAccountSerializer, \
    ActivateAccountSerializer, ForgetPasswordSerializer, ResetPasswordSerializer
from rest_framework.permissions import AllowAny

from .token import account_activation_token, password_reset_token

DOMAIN = settings.DOMAIN
PROTOCOL = settings.PROTOCOL
MAILJET_EMAIL = settings.MAILJET_EMAIL

from mailjet_rest import Client

mailjet = Client(auth=(settings.MAIL_JET_API_KEY, settings.MAIL_JET_API_SECRET), version='v3.1')


def send_mail(receiver_email, user, subject, template):
    message = render_to_string(template_name=template, context={
        'user': user,
        'protocol': PROTOCOL,
        'domain': DOMAIN,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })

    data = {
        'Messages': [
            {
                "From": {
                    "Email": MAILJET_EMAIL,
                    "Name": "Wings Box"
                },
                "To": [
                    {
                        "Email": receiver_email,
                        "Name": "Dear User"
                    }
                ],
                "Subject": subject,
                "TextPart": message,
                "HTMLPart": f"<h3>Dear {user.username}, Message: {message}",
                "CustomID": f"{receiver_email}"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print("account activation mail send")
    return result


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                print(user.email, user)
                send_mail(user.email, user, subject="Confirm Your Email", template='account/activate_account_mail.html')
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetails(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = [AccountDetailsSerializer]

    def get(self, request, *args, **kwargs):
        # print(request.user)
        ser = AccountDetailsSerializer(request.user)
        return Response(ser.data)


class ChangePasswordView(UpdateAPIView):
    queryset = Account.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(UpdateAPIView):
    queryset = Account.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateAccountSerializer


class AccountActivateView(APIView):
    serializer_class = ActivateAccountSerializer

    def post(self, request, *args, **kwargs):
        serializer = ActivateAccountSerializer(data=request.data)
        if serializer.is_valid():
            try:
                uid = force_text(urlsafe_base64_decode(serializer.data['uidb64']))
                user = Account.objects.get(pk=uid)

            except (TypeError, ValueError, OverflowError, Account.DoesNotExist) as e:
                user = None

            if user is not None and account_activation_token.check_token(user, serializer.data['token']):
                if user.is_active:
                    return Response("Account Verified Already", status=status.HTTP_202_ACCEPTED)
                user.is_active = True
                user.save()

                return Response("Account Verified Successfully", status=status.HTTP_202_ACCEPTED)
            else:
                return Response("Activation link expired activated", status=status.HTTP_403_FORBIDDEN)
        return Response("Account Activated")



class ForgetPasswordView(APIView):
    serializer_class = ForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = ForgetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = Account.objects.get(email=serializer.data['email'])
            except Exception as e:
                if e.args[0] == "Account matching query does not exist.":
                    return Response("Account not found with this email", status=status.HTTP_404_NOT_FOUND)
                print(e)

            send_mail(user.email, user, subject='Reset your Password',template='account/activate_account_mail.html')
            return Response("Password Reset Email is Send Successfully", status=status.HTTP_200_OK)


class ResetPasswordView(APIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data['uidb64'], serializer.data['token'], serializer.data['password1'],
                  serializer.data['password2'])
            try:
                uid = force_text(urlsafe_base64_decode(serializer.data['uidb64']))
                user = Account.objects.get(pk=uid)
                print("this iss it\n", uid, user)

            except (TypeError, ValueError, OverflowError, Account.DoesNotExist) as e:
                user = None

            if user is not None and account_activation_token.check_token(user, serializer.data['token']):
                if serializer.data['password1'] == serializer.data['password2']:
                    user.set_password(serializer.data['password2'])
                    user.save()
                    return Response("Password Reset Successfully", status=status.HTTP_202_ACCEPTED)

                return Response("Both passwords do not match", status=status.HTTP_206_PARTIAL_CONTENT)
            else:
                return Response("Activation link expired activated", status=status.HTTP_403_FORBIDDEN)
        return Response("Password Reset Successfully")
