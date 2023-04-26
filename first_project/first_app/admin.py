from django.contrib import admin
from first_app.models import Topic, WebPage, AccessRecord, Company,Employee

admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Company)
admin.site.register(Employee)
