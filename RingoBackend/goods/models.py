from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.



class GoodsCategory(models.Model):   
    """
    物品多级分类
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类目名", help_text="类目名")
    code = models.CharField(default="", max_length=30, verbose_name="类目代码", help_text="唯一类目代码")
    desc = models.TextField(default="", verbose_name="类目描述", help_text="类目描述")
    # 设置目录树的级别

    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    # 设置models有一个指向自己的外键
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "物品类目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Goods(models.Model):  
    """
    物品属性(提供/需求)
    """
    PROPERTY_TYPE = (
        (0, "需求物品"),
        (1, "提供物品"),
    )

    """
    物品种类
    """
    # CATEGORY_TYPE = (
    #     (0, "食品"),
    #     (1, "药品"),
    #     (2, "生活用品"),
    #     (3, "娱乐"),
    #     (4, "器械"),
    # )

    """
    需求紧急度
    """
    EMERGENCY_TYPE = (
        (1, "啥时候都行"),
        (2, "最好尽快"),
        (3, "比较紧急"),
        (4, "很急"),
        (5, "十万火急"),
    )


    property_type = models.IntegerField(choices=PROPERTY_TYPE, verbose_name="物品属性", help_text="物品是需求条目还是提供条目(0:需求 1:提供)")
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="物品类目",db_constraint=False)
    emergency = models.IntegerField(choices=EMERGENCY_TYPE, verbose_name="紧急度", default=1,help_text="紧急度(only 需求)")
    expected_end_time = models.DateTimeField(verbose_name="结束时间", default=datetime.now(), help_text="预期结束时间点(only 需求)")
    goods_sn = models.AutoField(primary_key=True, verbose_name="物品唯一编号")
    # user = models.CharField(max_length=50, default="", verbose_name="用户名")
    user = models.ForeignKey(User, on_delete=models.CASCADE,to_field='username', verbose_name=u"用户名", default='')

    name = models.CharField(max_length=100, verbose_name="物品名")
    address = models.TextField(max_length=100, verbose_name="地址",default='')
    goods_brief = models.TextField(max_length=100, verbose_name="物品简短描述",default='')
    goods_desc = models.TextField(max_length=500, verbose_name="物品详细描述", default='')
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")


    class Meta:
        verbose_name = '物品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name