from rest_framework import routers
from exams.api.views import ExamViewSet,SubCategoryViewSet
from subjects.api.views import SubjectViewSet,TopicsViewSet

routerV1 = routers.DefaultRouter()
routerV1.register(r'exams/sub-category/subjects/topics', TopicsViewSet)
routerV1.register(r'exams/sub-category/subjects', SubjectViewSet)
routerV1.register(r'exams/sub-category', SubCategoryViewSet)
routerV1.register(r'exams', ExamViewSet)

