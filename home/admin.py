from django.contrib import admin

from home.models import (
    Subject,
    Question,
    Option
)

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Option)
