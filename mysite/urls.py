from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('test/', views.test_page, name='test'),
    path('test/', views.test_page1, name='test'),
    # path('test1/', views.test_page1, name='test1'),
    path('test2/', views.test_page2, name='test2'),
    # path('test3/', views.test_page3, name='test3'),
    path('test4/', views.test_page4, name='test4'),
    # path('test5/', views.test_page5, name='test5'),
    path('test/result', views.result, name='result'),
    path('test2/result', views.result, name='result'),
    path('test4/result', views.result, name='result'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
