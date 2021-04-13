"""matProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from matematikProjectApp.views import mantıkProje
from users.views import Users
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mantıkProje.base),
    path("notbirak",mantıkProje.notOlustur,name="notbirak"),
    path("olustu",mantıkProje.notOlustur,name="olustu"),
    path("not_list",mantıkProje.not_list,name="not_list"),
    path("not_detail/<int:pk>/",mantıkProje.not_detail,name="post_detail"),
    path("not_delete/<int:pk>/",mantıkProje.not_delete,name="delete"),
    path("kayıtol",Users.user_register,name="kayıtol"),
    path("girisYap",Users.user_login,name="girisYap"),
    path("cikisYap",Users.user_cıkısYap,name="cikisYap")

]+static(settings.STATIC_URL,document_root = settings.STATICFILES_DIRS)
