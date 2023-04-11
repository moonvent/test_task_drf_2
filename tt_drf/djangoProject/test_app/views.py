from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from test_app.models import Entity
from test_app.serializers import EntitySerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = (IsAuthenticated,)

    def __add_user_before_update_model(self, 
                                       serializer):
        serializer.save(modified_by=self.request.user)

    def perform_create(self, serializer):
        self.__add_user_before_update_model(serializer=serializer)

    def perform_update(self, serializer):
        # answer on first question
        self.__add_user_before_update_model(serializer=serializer)

