from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home, detect, video_feed, start_stream, stop_stream, blog, register_user, login_user, logout_user, \
    detect_object, check_login_status

urlpatterns = [
    path('', home, name='home'),
    path('detect/', detect, name='detect'),
    path('detect_object/', detect_object, name='detect_object'),
    path('blog/', blog, name='blog'),
    path('login/', login_user, name='login'),
    path('check_login_status/', check_login_status, name='check_login_status'),
    path('register_user/', register_user, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('video_feed/', video_feed, name='video_feed'),
    path('start_stream/', start_stream, name='start_stream'),
    path('stop_stream/', stop_stream, name='stop_stream'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])