from django.contrib import admin

from .models import CustomUser, City, Subject, Comment

admin.site.register(CustomUser)
admin.site.register(City)
admin.site.register(Subject)
admin.site.register(Comment)
