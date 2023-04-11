from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from test_app.models import Entity
from test_app.serializers import EntitySerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=EntitySerializer,
        responses={status.HTTP_200_OK: EntitySerializer(many=True)},
        summary='Get list of available entity with their properties',
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        request=EntitySerializer,
        responses={status.HTTP_201_CREATED: EntitySerializer()},
        summary='Create a new entity object',
        )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def __add_user_before_update_model(self, 
                                       serializer):
        serializer.save(modified_by=self.request.user)

    def perform_create(self, serializer):
        self.__add_user_before_update_model(serializer=serializer)

    def perform_update(self, serializer):
        # answer on first question
        self.__add_user_before_update_model(serializer=serializer)

