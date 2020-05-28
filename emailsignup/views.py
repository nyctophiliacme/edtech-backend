from django.shortcuts import redirect
from rest_framework.decorators import api_view


@api_view()
def null_view(request):
    return redirect("https://www.superteacher.pk/not_found")


@api_view()
def complete_view(request):
    return redirect("https://www.superteacher.pk/")
