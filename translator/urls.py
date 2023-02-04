from . import views
from django.urls import path

from .views import translate_app

urlpatterns = [
    path('', views.translator_view, name='translator_view'),
    path('translate/', translate_app, name='trans')
]


