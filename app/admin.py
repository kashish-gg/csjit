from django.contrib import admin
from .models import post,topic,date
# Register your models here.
admin.site.register(post)
admin.site.register(topic)
admin.site.register(date)
admin.site.site_header='CSJIT'

