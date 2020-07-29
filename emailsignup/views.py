from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from emailsignup.models import CustomUser
from emailsignup.serializers import RequiredInformationSerializer
from rest_framework.response import Response
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


@api_view()
def null_view(request):
    return redirect("https://www.superteacher.pk/not_found")


@api_view()
def complete_view(request):
    return redirect("https://www.superteacher.pk/email_verified")


class CustomerRequiredInformationView(APIView):

    def get(self, request, *args, **kwargs):
        customers = CustomUser.objects.all().order_by('id')
        serializer = RequiredInformationSerializer(customers, many=True)
        return Response(serializer.data)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
