from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from dapi.settings import local
from django.conf.urls.static import static
from dapi.settings import settings
from django.conf.urls.static import static

urlpatterns = [
    
	#custom dapi
	path('api/v1/', include('apps.api.urls')),
	path('djrichtextfield/', include('djrichtextfield.urls')),

	
	#default
    path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)