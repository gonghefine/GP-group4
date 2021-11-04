from django.urls import path
from django.contrib import admin

import app.views


admin.autodiscover()


urlpatterns = [
    path('', app.views.index, name='index'),
    path('db/', app.views.db, name='db'),
    path('emissions/', app.views.emissions, name='emissions'),
    path('emissions/<int:page>', app.views.emissions, name='emissions'),
    path('aggregation/', app.views.aggregation, name='aggregation'),
    path('aggregation/<int:page>', app.views.aggregation, name='aggregation'),
    path('visual/', app.views.visual, name='visual'),
    path('fact_table/', app.views.fact_table, name='fact_table'),
    path('fact_table/<int:page>', app.views.fact_table, name='fact_table'),
    path('admin/', admin.site.urls),
]
