from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ReportViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'reports', ReportViewSet)


urlpatterns = [
    path('', include(router.urls))
]