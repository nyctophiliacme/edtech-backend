from help_request.models import HelpRequest
from help_request.serializers import HelpRequestSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from emailsignup.models import CustomUser


class HelpRequestView(APIView):

    def get(self, request, *args, **kwargs):
        help_requests_raised = HelpRequest.objects.all()
        serializer = HelpRequestSerializer(help_requests_raised, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = HelpRequestSerializer(data=request.data)
        if serializer.is_valid():
            if request.data.get("is_guest_user") == "true":
                user_obj = CustomUser.objects.get(email=request.data.get('user_email'))
                serializer.save(user=user_obj)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
