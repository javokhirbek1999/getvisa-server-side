from django.urls import path, include

from rest_framework.routers import DefaultRouter


from .views import job


router = DefaultRouter()
router.register(r'company', job.CompanyViewSet)
router.register(r'job', job.VacancyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]