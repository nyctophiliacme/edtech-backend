from allauth.account.views import ConfirmEmailView
from django.conf.urls import url, include
from django.urls import path
from emailsignup.views import complete_view, null_view, CustomerRequiredInformationView, \
    EmailVerifiedCustomerInformationView, UpdatePaymentStatusAsPaidView, UpdatePaymentStatusAsUnPaidView, FacebookLogin

urlpatterns = [
    # Override urls
    url(r'^registration/account-email-verification-sent/', null_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),
        name='account_confirm_email'),
    url(r'^registration/complete/$', complete_view, name='account_confirm_complete'),
    # Default urls
    url(r'^accounts/', include('allauth.urls')),

    path('password-reset/<uidb64>/<token>/', null_view, name='password_reset_confirm'),

    url(r'', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
    path('user/get_required_information/', CustomerRequiredInformationView.as_view()),
    path('user/get_verified_users/', EmailVerifiedCustomerInformationView.as_view()),
    path('user/update_payment_information/mark_as_paid/', UpdatePaymentStatusAsPaidView.as_view()),
    path('user/update_payment_information/mark_as_unpaid/', UpdatePaymentStatusAsUnPaidView.as_view()),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
]
