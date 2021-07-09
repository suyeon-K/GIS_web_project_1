from django.db import models

# Create your models here.

class NewModel(models.Model): # 장고에서 제공하는 기초 모델을 상속받아 모델 생성, ctrl + B를 누르면 장고는 오픈소스이기 때문에 코드가 어떻게 구성되어있는지 확인할 수 있다.
    text = models.CharField(max_length=255, null=False) # charfield 로 문자열을 받는다.
