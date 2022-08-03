from django.urls import path
from.views import postlistview
from . import views
urlpatterns = [
    path('', postlistview.as_view(),name="blog-home"),
    path('about/',views.about,name="blog-about"),

]