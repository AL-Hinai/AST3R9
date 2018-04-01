from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from AST3R9 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^AST3R9/', include('AST3R9.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)