from django.conf.urls import url, include
from django.contrib import admin


app_name = 'lista'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^', include('artists.urls')),

]
