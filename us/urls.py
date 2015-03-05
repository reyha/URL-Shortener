from django.conf.urls import patterns,url
from us import views

urlpatterns=patterns("",
                     url(r'^$','home'),
                     url(r'^(?P<id>[^/]+)/','link'),
                    
)
