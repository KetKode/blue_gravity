from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentApiViewSet, RegistrationView, RatingApiViewSet

router = DefaultRouter()

router.register(r"content", ContentApiViewSet, basename="content")
router.register(r"rating", RatingApiViewSet, basename="rating")

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("", include(router.urls)),
]
