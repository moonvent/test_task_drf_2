from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import APIException
from django.utils.translation import gettext as _
from test_app.models import Entity, Property


class PropertySerializer(serializers.ModelSerializer):
    # answer on third question
    class Meta:
        model = Property
        fields = ('key', 'value')


class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(required=False)
    properties = PropertySerializer(required=False,
                                    many=True,
                                    read_only=True)
    modified_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                                     required=False)

    class Meta:
        model = Entity
        fields = ('value', 
                  'properties', 
                  'modified_by')

    def run_validation(self, data: dict):
        # answer on second question

        if 'data[value]' in data:
            data['value'] = data.pop('data[value]')

        elif 'value' not in data:
            raise APIException(_("*value* field is required"))

        return super().run_validation(data)

