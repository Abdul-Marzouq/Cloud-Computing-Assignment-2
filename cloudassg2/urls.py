from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from login import views as login_views
from base import views
from imgmeta import views as img_views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^instructions/$',views.instruction,name='instructions'),
    url(r'^login/$',login_views.user_login,name='login'),
    url(r'^logout/$',login_views.user_logout, name='logout'),
    url(r'^admin/',admin.site.urls),
    url(r'^imgupload/$',img_views.imgupload,name='imgupload'),
    url(r'^imgsearch/$',img_views.imgsearch,name='imgsearch'),
    url(r'^imglist/$',img_views.imglist,name='imglist'),
    path('imgdelete/<delimageid>',img_views.imgdelete,name='imgdelete'),
    path('imgsearchres/<searchstr>',img_views.imgsearchres,name='imgsearchres'),
    url('^',include('django.contrib.auth.urls')),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
