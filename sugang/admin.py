from django.contrib import admin

# Register your models here.
from sugang.models import Subject, Take, Instructor

admin.site.register(Take)
admin.site.register(Subject)
admin.site.register(Instructor)
