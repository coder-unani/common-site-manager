from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "ORBITCODE 관리자 시스템";
admin.site.site_title = "SITE MANAGER";
admin.site.index_title = "ORBITCODE 관리도구"

urlpatterns = [
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contents/', include('contents.urls')),
]
