from rest_framework import serializers

from ..models import Employee


class FilterEmployeeListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)

        return serializer.data


class EmployeeSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterEmployeeListSerializer
        model = Employee
        fields = ('id', 'name', 'position', 'employment_date', 'salary', 'paid_salary', 'children', 'level')


class EmployeeDetailSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field='position', read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'position', 'employment_date', 'salary', 'paid_salary', 'parent', 'level')
