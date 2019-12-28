from django.contrib import admin
from test1.models import Question,Rating,UserProfileInfo
# Register your models here.
admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(UserProfileInfo)
admin.site.register(Rating)