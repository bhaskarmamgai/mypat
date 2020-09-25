from rest_framework import serializers
from subjects.models import Subject, Topics


class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['topics'] = TopicsSerializer(instance=instance.topics.all(), many=True).data,
        return response
