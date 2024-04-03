from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views, settings
from article import urls as articleUrls
from shop import urls as shopUrls
from service import urls as serviceUrls
from visitor import urls as visitorUrls
from _api import urls as apiUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
		path('articles/', include(articleUrls)),
		path('visitor/', include(visitorUrls)),
		path('shop/', include(shopUrls)),
		path('service/', include(serviceUrls)),
		path('api/', include(apiUrls)),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)