from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views, settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('home/', views.home,name='home'),
    path('',include('django.contrib.auth.urls')),
    path('register/',views.Register.as_view(),name='register'),
    path('',include('apps.posts.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
