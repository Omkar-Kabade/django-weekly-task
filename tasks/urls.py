from django.urls import path 
from . import views

#configuring subapps urls

urlpatterns = [
    path('' , views.index , name="index"),
    path("<int:day>", views.weekDayByNumber),
    path("<str:day>",views.weekDay , name = "week-day")
]
