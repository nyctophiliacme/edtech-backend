from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from emailsignup.models import CustomUser
from emailsignup.serializers import RequiredInformationSerializer
from rest_framework.response import Response
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import status
from allauth.account.admin import EmailAddress


@api_view()
def null_view(self, request, *args, **kwargs):
    return redirect("https://www.superteacher.pk/not_found")


@api_view()
def complete_view(request):
    return redirect("https://www.superteacher.pk/email_verified")


class CustomerRequiredInformationView(APIView):

    def get(self, request, *args, **kwargs):
        customers = CustomUser.objects.all().order_by('-id')
        serializer = RequiredInformationSerializer(customers, many=True)
        return Response(serializer.data)


class EmailVerifiedCustomerInformationView(APIView):

    def get(self, request, *args, **kwargs):
        verified_customer_ids = EmailAddress.objects.filter(verified=True).values_list('user_id', flat=True)
        customers = CustomUser.objects.filter(id__in=verified_customer_ids).order_by('-id')
        serializer = RequiredInformationSerializer(customers, many=True)
        return Response(serializer.data)


class UpdatePaymentStatusAsPaidView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(email=request.query_params.get("email_id"))
        except CustomUser.DoesNotExist:
            return Response("User not found", status=status.HTTP_400_BAD_REQUEST)

        if user.is_paid_user:
            return Response("User " + user.email + " has already a PAID account", status=status.HTTP_400_BAD_REQUEST)

        user.is_paid_user = True
        user.save()
        return Response("User " + user.email + " has now a PAID account", status=status.HTTP_201_CREATED)


class UpdatePaymentStatusAsUnPaidView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(email=request.query_params.get("email_id"))
        except CustomUser.DoesNotExist:
            return Response("User  " + request.query_params.get("email_id") + " not found",
                            status=status.HTTP_400_BAD_REQUEST)

        if not user.is_paid_user:
            return Response("User " + user.email + " has already an UNPAID account", status=status.HTTP_400_BAD_REQUEST)

        user.is_paid_user = False
        user.save()
        return Response("User " + user.email + " has now an UNPAID account", status=status.HTTP_201_CREATED)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
