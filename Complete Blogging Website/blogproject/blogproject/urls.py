"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from api.models import BookResource
#book_resource = BookResource()

# urls.py of your Django project

handler400 = 'blogapp.views.error_400'
handler403 = 'blogapp.views.error_403'
handler404 = 'blogapp.views.error_404'
handler500 = 'blogapp.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    path('blog/', include('blogapp.urls')),
    path('books/', include('blogapp.urls')),
    #path('api/', include(book_resource.urls))
]
