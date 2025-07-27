
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('replycontent/', views.reply_content, name='reply_content'),
    path('support_test/',views.support_test,name='support_test'),

]
