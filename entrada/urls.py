from django.conf import settings
from . import views
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns =[
    path('',views.index,name = 'index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.posts, name='posts'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
