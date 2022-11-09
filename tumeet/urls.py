from django.contrib import admin
from django.urls import path, include
from users.views import GithubLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/github/', GithubLogin.as_view())
]
