from django.urls import path
from.views import postlistview,postdetailview,postcreateview,postupdateview,postdeleteview,updatepostlistview
from . import views
urlpatterns = [
    path('', postlistview.as_view(),name="blog-home"),
    path('about/',views.about,name="blog-about"),
    path("post/<int:pk>/",postdetailview.as_view(),name="post-detail"),
    path("post/new/",postcreateview.as_view(),name="post-create"),
    path("post/<int:pk>/update/",postupdateview.as_view(),name="post-update"),
    path("post/<int:pk>/delete/",postdeleteview.as_view(),name="post-delete"),
    path('user/<str:username>', updatepostlistview.as_view(),name="user-post"),



]