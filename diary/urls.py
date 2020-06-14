from django.urls import path

from . import views

app_name = 'diary' # diaryアプリケーションのルーティング名
urlpatterns = [
    path('', views.IndexView.as_view(), name = "index"),
]