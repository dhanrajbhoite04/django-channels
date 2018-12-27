from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]