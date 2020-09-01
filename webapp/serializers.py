from cassandra.cqlengine import columns
from rest_framework import serializers
from .models import products, attributes


class productsSerializers(serializers.ModelSerializer):
    serializer_field_mapping = (
        serializers.ModelSerializer.serializer_field_mapping.copy()
    )
    serializer_field_mapping[columns.UUID] = columns.UUID

    # serializer_field_mapping[columns.Map] = columns.Map

    class Meta:
        model = products
        fields = '__all__'

    def to_representation(self, obj):
        attribs = []
        for attribute in obj.attributes:
            attribs.append({
                str(attribute): obj.attributes[attribute]
            })
        return {
            "id": str(obj.id),
            "attributes": attribs,
        }


class attributesSerializers(serializers.ModelSerializer):
    serializer_field_mapping = (
        serializers.ModelSerializer.serializer_field_mapping.copy()
    )
    serializer_field_mapping[columns.UUID] = columns.UUID

    name = serializers.CharField(
        style={'input_type': 'text'},
        trim_whitespace=True,
        max_length=None,
        min_length=None,
        allow_blank=False,
        required=True,
        label="Name",
        validators=[]
    )

    class Meta:
        model = attributes
        fields = '__all__'

    def to_representation(self, obj):
        return {
            "id": str(obj.id),
            "name": obj.name,
        }
