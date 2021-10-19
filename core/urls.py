from django.urls import path
from django.contrib import admin
from django.urls import path
from mysite.core import views

import app.views


admin.autodiscover()


urlpatterns = [
    path('', app.views.index, name='index'),
    path('db/', app.views.db, name='db'),
    path('emissions/', app.views.emissions, name='emissions'),
    path('emissions/<int:page>', app.views.emissions, name='emissions'),
    path('aggregation/', app.views.aggregation, name='aggregation'),
    path('aggregation/<int:page>', app.views.aggregation, name='aggregation'),
    
    path('pie-chart/', views.pie_chart, name='pie-chart')
    path('emissions/imo/', app.views.emission_detail, name='emission_detail'),
    path('emissions/imo/<int:imo>', app.views.emission_detail, name='emission_detail'),
    path('admin/', admin.site.urls),
]
