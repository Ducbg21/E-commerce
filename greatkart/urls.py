from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from . import views
from .app_list import APP_LIST

# URL để xử lý thay đổi ngôn ngữ
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# Các URL có hỗ trợ đa ngôn ngữ
i18n_urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]

# Thêm các app trong APP_LIST vào i18n_urlpatterns
for app, url in APP_LIST.items():
    i18n_urlpatterns.append(path(f'{url}', include(f'{app}.urls')))

# Thêm i18n_patterns vào urlpatterns
urlpatterns += i18n_patterns(*i18n_urlpatterns)

# Phục vụ file media trong khi dev
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
