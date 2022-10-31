from django.urls import path
from fusion import settings
from .views import IndexView
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
