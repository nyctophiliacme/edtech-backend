from django.urls import path
from help_request.views import HelpRequestView

urlpatterns = [
    path('raise_request/', HelpRequestView.as_view())
]
