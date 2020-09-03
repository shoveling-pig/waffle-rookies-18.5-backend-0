from django.urls import include, path
from rest_framework.routers import SimpleRouter
from survey.views import SurveyResultViewSet
from survey.views import OperatingSystemViewSet

app_name = 'survey'

router = SimpleRouter()
router.register('survey', SurveyResultViewSet, basename='survey')  # /api/v1/survey/
router.register('os', OperatingSystemViewSet, basename='os') # /api/vi/os/

urlpatterns = [
    path('', include((router.urls))),
]
