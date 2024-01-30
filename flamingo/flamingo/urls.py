from django.contrib import admin
from django.urls import path, include
from . import views
from article import urls as articleUrls
from _api import urls as apiUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
	path('articles/', include(articleUrls)),
	path('api/', include(apiUrls)),
]