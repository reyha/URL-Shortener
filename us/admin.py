from django.contrib import admin

# Register your models here.
from urlshortner.models import URL

class UrlAdmin(admin.ModelAdmin):

  list_display=["url"]

admin.site.register(URL,UrlAdmin)
