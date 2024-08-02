from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from core.models import ObjectType
from netbox.api.fields import ContentTypeField
from netbox.api.serializers import WritableNestedSerializer
from users.models import Group, ObjectPermission, Token, User

__all__ = [
    'NestedGroupSerializer',
    'NestedObjectPermissionSerializer',
    'NestedTokenSerializer',
    'NestedUserSerializer',
]


class NestedGroupSerializer(WritableNestedSerializer):

    class Meta:
        model = Group
        fields = ['id', 'url', 'display_url', 'display', 'name']


class NestedUserSerializer(WritableNestedSerializer):

    class Meta:
        model = User
        fields = ['id', 'url', 'display_url', 'display', 'username']

    @extend_schema_field(OpenApiTypes.STR)
    def get_display(self, obj):
        if full_name := obj.get_full_name():
            return f"{obj.username} ({full_name})"
        return obj.username


class NestedTokenSerializer(WritableNestedSerializer):

    class Meta:
        model = Token
        fields = ['id', 'url', 'display_url', 'display', 'key', 'write_enabled']


class NestedObjectPermissionSerializer(WritableNestedSerializer):
    object_types = ContentTypeField(
        queryset=ObjectType.objects.all(),
        many=True
    )
    groups = serializers.SerializerMethodField(read_only=True)
    users = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ObjectPermission
        fields = [
            'id', 'url', 'display_url', 'display', 'name', 'enabled', 'object_types', 'groups', 'users', 'actions'
        ]

    @extend_schema_field(serializers.ListField)
    def get_groups(self, obj):
        return [g.name for g in obj.groups.all()]

    @extend_schema_field(serializers.ListField)
    def get_users(self, obj):
        return [u.username for u in obj.users.all()]
