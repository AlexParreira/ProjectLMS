
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from core import views

admin.site.site_header = 'LMS Adminsitration'                  
admin.site.index_title = 'Features area'                 
admin.site.site_title = 'LMS adminsitration' 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]
