from allauth.account.views import ConfirmEmailView
from django.conf.urls import url, include
from django.urls import path
from emailsignup.views import complete_view, null_view, CustomerRequiredInformationView, \
    EmailVerifiedCustomerInformation, FacebookLogin

urlpatterns = [
    # Override urls
    url(r'^registration/account-email-verification-sent/', null_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^registration/complete/$', complete_view, name='account_confirm_complete'),
    # Default urls
    url(r'^accounts/', include('allauth.urls')),
    url(r'', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
    path('user/get_required_information', CustomerRequiredInformationView.as_view()),
    path('user/get_verified_users', EmailVerifiedCustomerInformation.as_view()),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
]
