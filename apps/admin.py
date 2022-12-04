from django.contrib import admin

from .models.job import Vacancy, Company


# Register your models here.
admin.site.register(Company)
admin.site.register(Vacancy)