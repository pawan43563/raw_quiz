from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class QuestionResource(resources.ModelResource):

    class Meta:
        model = Question


class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource

class AnswerResource(resources.ModelResource):

    class Meta:
        model = Answer


class AnswerAdmin(ImportExportModelAdmin):
    resource_class = AnswerResource

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)