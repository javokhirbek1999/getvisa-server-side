from rest_framework import viewsets


from ..models.job import Company, Vacancy
from ..serializers.job import CompanySerializer, VacancySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

