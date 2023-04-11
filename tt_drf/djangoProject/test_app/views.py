from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from test_app.models import Entity
from test_app.serializers import EntitySerializer

from drf_yasg.utils import swagger_auto_schema


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(operation_description='Get list of all entities with their properties',
                         responses={status.HTTP_200_OK: EntitySerializer},
                         )
    @action(detail=True, 
            methods=['get'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description='Create a new enitity with need data',
                         responses={status.HTTP_201_CREATED: EntitySerializer},
                         )
    @action(detail=True, 
            methods=['post'])
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

