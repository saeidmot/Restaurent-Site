from django.db import models
from django.utils.translation import gettext as _   #for persian text

# Create your models here.
class Food(models.Model):
    FOODS=[
        ('iranianfood','غذای ایرانی'),
        ('fastfood','فست فود'),
        ('juices','نوشیدنی'),
    ]

    name=models.CharField(_('نام غذا'),max_length=100)
    text=models.CharField(_('توضیحات'),max_length=50)
    price=models.IntegerField(_('قیمت'),default=100000)
    time = models.IntegerField(_('زمان آماده شدن غذا'),default=2)
    created=models.DateTimeField(_('تاریخ انتشار'),auto_now_add=True)
    image=models.ImageField(_('تصویر غذا'),upload_to='webs/')
    type=models.CharField(_('نوع غذا'),max_length=50,choices=FOODS,default='fastfood')

    def __str__(self):
        return self.name


