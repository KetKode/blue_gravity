from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from models import Content
from serializers import ContentSerializer
from drf_spectacular.utils import extend_schema
from schema_data import CONTENT_API_METADATA


class ContentApiViewSet(ModelViewSet):
    queryset = Content.objects.all()
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
