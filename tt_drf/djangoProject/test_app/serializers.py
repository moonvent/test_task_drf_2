from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import APIException
from django.utils.translation import gettext as _
from test_app.models import Entity, Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(required=False)
    properties = PropertySerializer(required=False,
                                    many=True, 
                                    read_only=True)
    modified_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                                     required=False)

    class Meta:
        model = Entity
        # fields = ('id', 
        #           'value',
        #           'properties')
        fields = '__all__'

    def run_validation(self, data=...):
        # answer on second question

        try:
            data['value'] = data.pop('data[value]')

        except KeyError:
            raise APIException(_("*value* field is required"))

        return super().run_validation(data)

    def create(self, validated_data):
        return super().create(validated_data)

