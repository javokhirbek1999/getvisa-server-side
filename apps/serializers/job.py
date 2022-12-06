from rest_framework.serializers import ModelSerializer, DictField, FileField

from ..models.job import Company, Vacancy



class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'logo')
    

class VacancySerializer(ModelSerializer):

    title = DictField(source='getTitle')
    country = DictField(source='getCountry')
    currency = DictField(source='getCurrency')
    rate = DictField(source='getRate')
    work_schedule = DictField(source='getWorkSchedule')
    description = DictField(source='getDescription')

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'companyInfo', 'country', 'salary', 'currency', 'rate', 'work_schedule', 'description', 'minAge', 'maxAge', 'thumbnail')
    