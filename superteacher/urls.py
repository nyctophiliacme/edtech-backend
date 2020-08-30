"""superteacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

import emailsignup.urls
import exams.urls
import subjects.urls
import chapters.urls
import questions.urls
import user_question.urls
import courses.urls
import exam_details.urls
import help_request.urls

urlpatterns = [
    path('api/auth/', include(emailsignup.urls)),
    path('api/admin/', admin.site.urls),
    path('api/exams/', include(exams.urls)),
    path('api/subjects/', include(subjects.urls)),
    path('api/chapters/', include(chapters.urls)),
    path('api/questions/', include(questions.urls)),
    path('api/user_progress/', include(user_question.urls)),
    path('api/courses/', include(courses.urls)),
    path('api/exam_data/', include(exam_details.urls)),
    path('api/help/', include(help_request.urls)),
]
