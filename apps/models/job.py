from django.db import models
from django.conf import settings

from ckeditor.fields import RichTextField


COUNTRIES = {
    'POLAND': {
        'UZ': 'POLSHA',
        'RU': 'Польша',
        'EN': 'POLAND'
    },

    'SERBIA': {
        'UZ': 'SERBIYA',
        'RU': 'СЕРБИЯ',
        'EN': 'SERBIA',
    },

    'SLOVAKIA': {
        'UZ': 'SLOVAKIYA',
        'RU': 'СЛОВАКИЯ',
        'EN': 'SLOVAKIA'
    },

    'CROATIA': {
        'UZ': 'XORVATIYA',
        'RU': 'ХОРВАТИЯ',
        'EN': 'CROTIA'
    }
}

COUNTRY_CHOICES = [
    ('POLAND','POLAND'),
    ('SERBIA','SERBIA'),
    ('SLOVAKIA','SLOVAKIA'),
    ('CROATIA','CROATIA')
]


def company_upload_to(instance, filename):
    return "company/{filename}".format(filename=filename)

def vacancy_upload_to(instance, filename):
    return "vacancy/{filename}".format(filename=filename)


class Company(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to=company_upload_to, default='company/default_company_thumbnail.jpg')

    class Meta:
        verbose_name_plural='Companies'
    

    def __str__(self) -> str:
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=250)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    country = models.CharField(max_length=250, choices=COUNTRY_CHOICES)
    salary = models.DecimalField(max_digits=250, decimal_places=2)
    currency = models.CharField(max_length=250)
    rate = models.CharField(max_length=250)
    work_schedule = RichTextField(blank=True)
    description = RichTextField(blank=True)
    minAge = models.IntegerField(default=0)
    maxAge = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to=vacancy_upload_to, default='vacancy/default_vacancy_thumbnail.jpg')

    class Meta:
        verbose_name_plural='Vacancies'

    def __str__(self) -> str:
        return f'{self.id} | {self.title} | {self.company.name} | {self.salary} {self.currency}/{self.rate}'
    
    @property
    def getTitle(self):
        titleAll = self.title.split("|")
        languages = len(titleAll)
        return {
            'UZ': titleAll[0] if languages >= 1 else '',
            'RU': titleAll[1] if languages >= 2 else '',
            'EN': titleAll[2] if languages > 2 else ''
        }
    

    @property
    def getCountry(self):
        return COUNTRIES[self.country]
    
    @property
    def getCurrency(self):
        currencies = self.currency.split('|')
        allCurrencies = len(currencies)
        return {
            'UZ': currencies[0] if allCurrencies >= 1 else '',
            'RU': currencies[1] if allCurrencies >= 2 else '',
            'EN': currencies[2] if allCurrencies > 2 else '' 
        }
    
    @property
    def getRate(self):
        ratesAll = self.rate.split("|")
        rates = len(ratesAll)
        return {
            'UZ': ratesAll[0] if rates >= 1 else '',
            'RU': ratesAll[1] if rates >= 2 else '',
            'EN': ratesAll[2] if rates > 2 else ''
        }
    

    @property
    def getWorkSchedule(self):
        workSchedulesAll = self.work_schedule.split("<hr />")
        allWS = len(workSchedulesAll)
        return {
            'UZ': workSchedulesAll[0] if allWS >= 1 else '',
            'RU': workSchedulesAll[1] if allWS >= 2 else '',
            'EN': workSchedulesAll[2] if allWS > 2 else ''
        }
    
    
    @property
    def getDescription(self):
        allDescriptions = self.description.split("<hr />")
        allDescription = len(allDescriptions)
        return {
            'UZ': allDescriptions[0] if allDescription >= 1 else '',
            'RU': allDescriptions[1] if allDescription >= 2 else '',
            'EN': allDescriptions[2] if allDescription > 2 else ''
        }


    @property
    def companyInfo(self):
        absolute_url = settings.DEFAULT_DOMAIN + self.company.logo.url
        return {
            'id': self.company.id,
            'name': self.company.name,
            'logo': absolute_url
        }
