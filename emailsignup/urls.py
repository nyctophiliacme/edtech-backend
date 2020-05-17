from django.conf.urls import url, include
from allauth.account.views import ConfirmEmailView
from .views import complete_view, null_view

urlpatterns = [
    # Override urls
    url(r'^registration/account-email-verification-sent/', null_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^registration/complete/$', complete_view, name='account_confirm_complete'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', null_view, name='password_reset_confirm'),
    # Default urls
    url(r'', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls'))
]
