from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('testimonials/', include('testimonials.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = "smart_cctv.views.handler403"
handler404 = "smart_cctv.views.handler404"
handler500 = "smart_cctv.views.handler500"
