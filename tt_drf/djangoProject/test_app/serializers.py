from rest_framework import serializers

from test_app.models import Entity


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        # fields = ('id', 'value')
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)

