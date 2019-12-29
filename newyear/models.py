from django.db import models
from db.base_model import BaseModel
# Create your models here.

class cateType(BaseModel):
    '''奖品等级模型类'''
    cate = models.CharField(max_length=20, verbose_name='奖品等级')
    count = models.IntegerField(verbose_name='奖品个数')
    desc = models.CharField(max_length=200, verbose_name='奖品描述')
    index = models.IntegerField(verbose_name='数字越大越靠前')

    class Meta:
        db_table = 'df_cate'
        verbose_name = '奖品等级'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cate


class UserInfo(BaseModel):
    '''用户模型类'''
    type = models.ForeignKey('cateType', verbose_name='奖品等级',on_delete=models.DO_NOTHING, null=True,blank=True)
    name = models.CharField(max_length=50, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='联系电话',unique=True)
    is_default = models.BooleanField(default=False, verbose_name='是否备选')
    class Meta:
        db_table = 'df_userinfo'
        verbose_name = '会员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name