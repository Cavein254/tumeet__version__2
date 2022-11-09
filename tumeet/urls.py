from django.contrib import admin
from django.urls import path, include
import urllib.parse
from django.shortcuts import redirect
from allauth.socialaccount.providers.github import views as github_views
from users.views import GithubLogin
from users.views import Home # new

def github_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'http://127.0.0.1:8000/auth/github?{params}')

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/github/url/', github_views.oauth2_login),
    path('accounts/', include('allauth.urls')),
    path('', GithubLogin.as_view()),
    path('auth/github/callback/', github_callback, name='github_callback'),
]


