from rest_framework.serializers import ModelSerializer

from ..models.job import Company, Vacancy



class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name')
    

class VacancySerializer(ModelSerializer):

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'companyInfo', 'country', 'salary', 'currency', 'rate', 'description')