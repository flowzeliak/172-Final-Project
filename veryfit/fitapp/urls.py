from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('exertype/', views.exertype, name='exertype'),
    path('exerlog/', views.exerlog, name='exerlog'),
    path('detlog/<int:id>', views.detlog, name='detlog'),
    path('newType/', views.newType, name='newtype'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]
