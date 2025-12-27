
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/', include('default.urls')),
    path('',RedirectView.as_view(url='message/')),
    path('account/', include('django.contrib.auth.urls')),
]
