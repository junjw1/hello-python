from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from todo.models import Todo

class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vueonly.html'


# 필요한 속성들을 오버라이딩
class TodoCV(CreateView):
    model = Todo # 테이블
    fields = '__all__' # 폼을 만들기 위해 필드 필요. 모든 필드 사용
    template_name = 'todo/todo_form.html' # redirectView를 제외한 모든 뷰에서 사용되는 속성
    success_url = reverse_lazy('todo:list') # 리다이렉트 시킬 url


class TodoLV(ListView):
    model = Todo # 테이블
    template_name = 'todo/todo_list.html'


class TodoDelV(DeleteView):
    model = Todo # 특정 레코드를 삭제해야하므로 모델로 테이블을 지정
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:list') # reverse() 또는 reverse_lazy() 사용해야. reverse()는 해당 라인 실행 시점 시작 시 urls.py가 로딩이 안된 상태..?? 뭐징