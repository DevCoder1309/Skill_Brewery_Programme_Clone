from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('def', views.page_1, name="page_1"),
    path('cel', views.page_2, name="page_2"),
    path('termsofservice', views.page_3, name="page_3"),
    path('email', views.email, name="email"),
]