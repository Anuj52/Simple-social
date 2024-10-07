from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'simplesocial'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('test/', views.TestPage.as_view(), name='test'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('groups/', include('groups.urls', namespace='groups')),
    path('accounts/', include('django.contrib.auth.urls')), 
]
