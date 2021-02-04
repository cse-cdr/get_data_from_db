from django.urls import path
from practwo1.views import index
from practwo1 import views
urlpatterns = [
    path('', views.index,name='index'),
    path('detail',views.detail,name='detail')
]