from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('arrivals', views.arrivals),
    path('kid', views.kid),
    path('lifesty', views.lifesty),
    path('menchoose', views.menchoice),
    path('mensport', views.mensport),
    path('privacy', views.privacy),
    path('refund', views.refund),
    path('sandel', views.sandel),
    path('term', views.term),
    path('walking', views.walking),
    path('women', views.women),
    path('womenstyle', views.womenstyle),
    path('womentrain', views.womentrain),
    path('womenwalk', views.womenwalk),
    path('product/<int:id>', views.product),
    path('login', views.login),
    path('signup', views.signup),
    path('logout',views.logout)
]
