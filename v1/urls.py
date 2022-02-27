#from django.contrib import admin
from django.urls import path
from v1 import views

app_name = 'v1'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/Score_Card', views.CardList.as_view()),
]
