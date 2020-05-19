from django.conf.urls import url, include
from allauth.account.views import ConfirmEmailView
from .views import complete_view, null_view

urlpatterns = [
    # Override urls
    url(r'^registration/account-email-verification-sent/', null_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^registration/complete/$', complete_view, name='account_confirm_complete'),
    # Default urls
    url(r'^accounts/', include('allauth.urls')),
    url(r'', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls'))
]
