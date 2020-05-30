
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from article import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("articles/",include("article.url"),name="dashboard"),
    path("user/",include("user.url")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     