from django.contrib import admin

# Register your models here.
from us.models import URL

class UrlAdmin(admin.ModelAdmin):

  list_display=["url"]

admin.site.register(URL,UrlAdmin)
