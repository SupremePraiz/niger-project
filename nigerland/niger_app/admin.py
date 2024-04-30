from django.contrib import admin

from .models import Surveyor, Documents

# Register your models here.
class SurveyorAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    
class SurveyorDocument(admin.ModelAdmin):
    list_display = ["user", "surveyor", "file"]

admin.site.register(Surveyor, SurveyorAdmin)
admin.site.register(Documents, SurveyorDocument)