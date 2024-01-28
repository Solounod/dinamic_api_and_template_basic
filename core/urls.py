
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('api/products/', include('apps.products.urls')),
    path('api/services/', include('apps.services.urls')),
    path('api/blog/', include('apps.blog.urls')),
    path('api/users/', include('apps.users.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += [re_path(r'^.*',
#                        TemplateView.as_view(template_name='index.html')),
#                        ]
