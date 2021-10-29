from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from imager.api.views import SnippetsViewSet

router = routers.DefaultRouter()
router.register(r'snippets', SnippetsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
