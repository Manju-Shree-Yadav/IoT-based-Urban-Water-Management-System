from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('map/', views.map, name="map"),
    path('turbidity/', views.turbidity, name="turbidity"),
    path('turgraph/', views.turgraph, name="turgraph"),
    path('flowrate/', views.flowrate, name="flowrate"),
    path('moisture/', views.moisture, name="moisture"),
    path('levelrange/', views.levelrange, name="levelrange"),
    path('sensortable/', views.sensortable, name="sensortable"),
    path('passage/', views.passage, name="passage"),
    path('map2/', views.map2, name="map2"),
    re_path(
        r'^(?P<sensor1>[0-9]+(?:\.[0-9]+)?)/(?P<sensor2>[0-9]+(?:\.[0-9]+)?)/(?P<sensor3>[0-9]+(?:\.[0-9]+)?)/(?P<sensor4>[0-9]+(?:\.[0-9]+)?)/(?P<sensor5>[0-9]+(?:\.[0-9]+)?)/(?P<sensor6>[0-9]+(?:\.[0-9]+)?)/(?P<time>[A-Za-z]{3} [A-Za-z]{3} [012]?[0-9] [012]?[0-9]:[0-5][0-9]:[0-5][0-9] [0-9]{4})/$',
        views.Display,
        name="Display"
    ),
]
