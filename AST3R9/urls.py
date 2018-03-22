from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from AST3R9 import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^AST3R9/', include('AST3R9.urls')),
# above maps any URLs starting
# with rango/ to be handled by
# the rango application
url(r'^admin/', admin.site.urls),
]