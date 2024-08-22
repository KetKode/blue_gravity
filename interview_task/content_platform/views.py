from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .models import Content, Rating
from .serializers import ContentSerializer, UserSerializer, RatingSerializer
from drf_spectacular.utils import extend_schema
from .schema_data import CONTENT_API_METADATA, RATING_API_METADATA


class ContentApiViewSet(ModelViewSet):
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContentSerializer

    @extend_schema(**CONTENT_API_METADATA["ContentCreate"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(**CONTENT_API_METADATA["ContentList"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(**CONTENT_API_METADATA["ContentRetrieve"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(**CONTENT_API_METADATA["ContentUpdate"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(**CONTENT_API_METADATA["ContentUpdate"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(**CONTENT_API_METADATA["ContentDestroy"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class RatingApiViewSet(ModelViewSet):
    queryset = Rating.objects.select_related("content", "rated_by").all()
    permission_classes = [IsAuthenticated]
    serializer_class = RatingSerializer

    @extend_schema(**RATING_API_METADATA["RatingCreate"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(**RATING_API_METADATA["RatingList"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(**RATING_API_METADATA["RatingRetrieve"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(**RATING_API_METADATA["RatingUpdate"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(**RATING_API_METADATA["RatingUpdate"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(**RATING_API_METADATA["RatingDestroy"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
