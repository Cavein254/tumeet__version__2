from django.contrib import admin
from django.urls import path, include
from users.views import GithubLogin
import urllib.parse
from django.shortcuts import redirect
from allauth.socialaccount.providers.github import views as github_views

def github_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'http://localhost:8000/auth/github?{params}')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/github/', GithubLogin.as_view()),
    path('auth/github/url/', github_views.oauth2_login)
]
