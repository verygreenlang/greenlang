"""matcherapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import os

import environ
from django.contrib import admin
from django.urls import include, path, re_path
from form2metrics.views import hello_world,hello_request,hello_submitted
from testscheduler.views import hello_mail
env = environ.Env()

version_number = "api/v1/"
investor_routes = version_number + "matcher/"
urlpatterns = [
    path(env("secret_admin_url") + "/", admin.site.urls),
    path(version_number+"auth/", include("djoser.urls")),
    path(version_number+"auth/", include("djoser.urls.jwt")),
    path("", include("health_check.urls")),

]

if env("DEBUG") and env("ENV") == "local":
    redoc_url_base_path = env("doc_path") + "/"
    urlpatterns.append(path(redoc_url_base_path, include("doc.urls")))
    urlpatterns.append(path(investor_routes + "form/task", hello_world))
    urlpatterns.append(path(investor_routes + "form/submitted", hello_submitted))
    urlpatterns.append(path(investor_routes + "mail/basic", hello_mail))
    urlpatterns.append(path(investor_routes + "form/requestform_mail",hello_request))
