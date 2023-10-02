from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('welcome/', views.welcome_page, name='welcome_page'),
    path('',views.LoginPage,name='singup'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('content/<int:item_id>/', views.item_conteudo_detail, name='item_conteudo_detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)