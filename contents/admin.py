from django.contrib import admin

from .models import Content, ContentAttach, ContentCategory

# Register your models here.
admin.site.register(ContentAttach)
admin.site.register(Content)
admin.site.register(ContentCategory)