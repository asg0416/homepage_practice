from django.db import models

# Create your models here.

class Memo(models.Model):
    title = models.CharField('제목',max_length=200)
    desc = models.TextField('본문',blank=True) #blank는 빈칸으로 제출해도 에러 안띄움
    pic = models.ImageField('사진', blank=True, null=True)
    created_at = models.DateTimeField('생성날짜', auto_now_add=True) #생설될때 픽스됨
    modified_at = models.DateTimeField('수정날짜', auto_now=True) #수정할때마다 바뀜

    # 마이그레이션이란 orm 을 통해 파이썬 데이터들의 클래스를 문서화 시켜준 것이다.

    def __str__(self):
        return self.title
    