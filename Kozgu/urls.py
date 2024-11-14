
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# Set up the schema view for API documentation
schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="This is the API documentation for the Blog project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myblog.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Apps.apis.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
