from django.contrib import admin

from todo.models import Todo

# Register your models here.
# 테이블 신규 정의 시 admin 사이트에서도 보이도록 등록

@admin.register(Todo) # 등록 위한 데코레이트
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'todo') # admin 사이트에서 보여줄 컬럼들