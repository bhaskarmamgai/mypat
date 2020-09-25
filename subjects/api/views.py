from rest_framework import viewsets
from subjects.api.serializers import SubjectsSerializer, TopicsSerializer
from subjects.models import Subject, Topics


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.filter(is_deleted=False, is_active=True, sub_category__is_deleted=False).order_by('-id')
    serializer_class = SubjectsSerializer
    http_method_names = ['post','get']
    """
    curl --location --request POST 'http://localhost:8000/api/v1/exams/sub-category/subjects/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: csrftoken=0EYWxNuTBOn44ce7U2v3803zspfLzNK1UJ36yiS3AsdDavYXR0lDqtzJYH46wZTG' \
    --data-raw '{
        "code": "MOMT",
        "name": "MATH",
        "sub_category": 2
    }'
    """


class TopicsViewSet(viewsets.ModelViewSet):
    queryset = Topics.objects.filter(is_deleted=False, is_active=True, subject__is_deleted=False).order_by('-id')
    serializer_class = TopicsSerializer
    http_method_names = ['post','get']

    """
    curl --location --request POST 'http://localhost:8000/api/v1/exams/sub-category/subjects/topics/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: csrftoken=0EYWxNuTBOn44ce7U2v3803zspfLzNK1UJ36yiS3AsdDavYXR0lDqtzJYH46wZTG' \
    --data-raw '{
        "name": "Linear Algebra",
        "subject": 1
    }'
    """
