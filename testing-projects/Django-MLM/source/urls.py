from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerce/', include('ecommerce.urls')),
    path('binary-plan/', include('binary_plan.urls')),
    path('level-plan/', include('level_plan.urls')),
    path('authentication/', include('authentication.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)