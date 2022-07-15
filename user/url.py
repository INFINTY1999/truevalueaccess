from . import views
from django.urls import path

urlpatterns = [

    path('users',views.user.as_view(),name='user class'),
    path('users/{<int:pk>}',views.userid.as_view(),name='user class'),

]