from django.urls import path

from . import views

app_name = 'diary' # diaryアプリケーションのルーティング名
urlpatterns = [
    path('', views.IndexView.as_view(), name = "index"),
    path('inquiry/', views.IndexView.as_view(), name="inquiry"), # 問い合わせ用のルーティングを追加
]