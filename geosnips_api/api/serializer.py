from rest_framework import serializers
from .models import features,geometry,properties

class GeometrySerializer(serializers.ModelSerializer):
    class Meta:
        model = geometry
        fields = "__all__"
class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = properties
        fields = ("name","country","ISO3166-1-Alpha-3","state_code","id")
        extra_kwargs = {
            'ISO3166-1-Alpha-3': {'source': 'ISO'},
        }
class FeatureSerializer(serializers.ModelSerializer):
    geometry = GeometrySerializer(many=False, read_only=False)
    properties = PropertiesSerializer(many=False, read_only=False)
    class Meta:
        model = features
        fields = ('type', 'properties', 'geometry')
    
    def create(self, validated_data):
        geometry_data = validated_data.pop('geometry')
        properties_data = validated_data.pop('properties')
        geometry_obj = GeometrySerializer.create(GeometrySerializer(), validated_data=geometry_data)
        properties_obj = PropertiesSerializer.create(PropertiesSerializer(), validated_data=properties_data)
        feature_obj = features.objects.create(**validated_data, geometry=geometry_obj, properties=properties_obj)
        return feature_obj