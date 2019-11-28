from django.urls import path
from . import views

app_name = 'todo' # 앱 네임 스페이스
urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name='vonly'), # todo 다음에 vonly라는 url이 들어왔을때, 뷰 이름은 TodoVueOnlyTV, url 패턴 이름은 vonly

    path('create/', views.TodoCV.as_view(), name='create'),
    path('list/', views.TodoLV.as_view(), name='list'),
    path('<int:pk>/delete/', views.TodoDelV.as_view(), name='delete'), # path convert. 숫자가 들어오면 정수로 변환하여 뷰로 넘겨줌.
]
