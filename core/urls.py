
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('replycontent', views.reply_content, name='reply_content'),

]
