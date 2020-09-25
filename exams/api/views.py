from rest_framework import viewsets
from exams.api.serializers import ExamSerializer, SubCategorySerializer
from exams.models import Exams, SubCategory


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exams.objects.filter(is_deleted=False, is_active=True).order_by('-id')
    serializer_class = ExamSerializer
    http_method_names = ['post', 'get']

    """
    curl --location --request POST 'http://localhost:8000/api/v1/exams/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: csrftoken=0EYWxNuTBOn44ce7U2v3803zspfLzNK1UJ36yiS3AsdDavYXR0lDqtzJYH46wZTG' \
    --data-raw '{
        "code": "DCS-002",
        "name": "Digital Signature",
    }'
    """


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.filter(is_deleted=False, is_active=True).order_by('-id')
    serializer_class = SubCategorySerializer
    http_method_names = ['post']
    """
    curl --location --request POST 'http://localhost:8000/api/v1/exams/sub-category/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: csrftoken=0EYWxNuTBOn44ce7U2v3803zspfLzNK1UJ36yiS3AsdDavYXR0lDqtzJYH46wZTG' \
    --data-raw '{
        "name": "IITM2",
        "exam":1
    }'
    """
