from django.views.generic import TemplateView

class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vueonly.html'