from django.urls import path
from mi_app import views
from .views import home, test


urlpatterns = [
    path('', home, name="home",),
    path('test/', test, name="test"),
]
