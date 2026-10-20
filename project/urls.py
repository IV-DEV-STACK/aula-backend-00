
from django.contrib import admin
from django.urls import path
from catalogo.views import home, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path('sobre', sobre)
]
