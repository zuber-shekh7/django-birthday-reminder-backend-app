from birthday_reminder_project.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('birthdays/', include('birthdays.urls')),
    path('api/accounts/signin/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/accounts/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
