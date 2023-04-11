from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from test_app.models import Entity
from test_app.serializers import EntitySerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        # answer on first question
        serializer.save(modified_by=self.request.user)

