from django.db import models

# Create your models here.
# 모델 Todo 정의
class Todo(models.Model):
    name = models.CharField('NAME', max_length=5, blank=True)
    todo = models.CharField('TODO', max_length=50)

    def __str__(self):
        return self.todo

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None): # save 메서드 오버라이딩
        if not self.name: # 이름 디폴트 값 설정. db 저장 시 넣는게 일반적.
            self.name = '홍길덩'
        super().save() # 상위 클래스의 save 호출
