from rest_framework import serializers
from exams.models import Exams, SubCategory
from subjects.api.serializers import SubjectsSerializer

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['subjects'] = SubjectsSerializer(instance=instance.subjects.all(), many=True).data,
        return response


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exams
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['sub_categories'] = SubCategorySerializer(instance=instance.subcategories.all(), many=True).data,
        return response
