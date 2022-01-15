from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

# Loading plotly Dash apps script
from django.urls import path

from . import views


urlpatterns = [
   path('', views.index, name='liverpool_goals'),
    # path('choose/match/',views.choose_match,name='index')
   #  path('test/',views.test)
    
    ]