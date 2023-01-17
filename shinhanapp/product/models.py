from django.db import models

# Create your models here.

class Product(models.Model):
    #title, content, price, location
    title = models.CharField(max_length=128, verbose_name="상품명")
    content = models.TextField(verbose_name="상품내용")
    price = models.IntegerField(verbose_name="가격")
    location = models.CharField(max_length=256, verbose_name="위치")
    image = models.FileField(null=True, blank=True, verbose_name="이미지")


    class Meta: # 자동으로 생성되는 것을 지정해주기 위한 클래스
        db_table = 'shinhan_product' # 원하는 table명으로 지정
        verbose_name = '상품'
        verbose_name_plural = '상품'