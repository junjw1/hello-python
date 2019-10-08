from django.urls import path
from . import views

app_name = 'todo' # 앱 네임 스페이스
urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name='vonly'), #todo 다음에 vonly라는 url이 들어왔을때, 뷰 이름은 TodoVueOnlyTV, url 패턴 이름은 vonly
]
