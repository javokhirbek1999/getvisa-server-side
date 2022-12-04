from django.db import models
from ckeditor.fields import RichTextField

class Company(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural='Companies'
    

    def __str__(self) -> str:
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=250)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    country = models.CharField(max_length=250)
    salary = models.DecimalField(max_digits=250, decimal_places=2)
    currency = models.CharField(max_length=250)
    rate = models.CharField(max_length=250)
    description = RichTextField(blank=True)


    class Meta:
        verbose_name_plural='Vacancies'

    def __str__(self) -> str:
        return f'{self.id} | {self.title} | {self.company.name} | {self.salary} {self.currency}/{self.rate}'
    
    @property
    def companyInfo(self):
        return {
            'id': self.company.id,
            'name': self.company.name
        }

