from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
from tyadmin_api_cli.fields import richTextField

User = get_user_model()


class GoodsCategory(models.Model):   
    """
    物品多级分类
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别代码", help_text="唯一类别代码")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    # 设置目录树的级别

    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    # 设置models有一个指向自己的外键
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目级别",
                                        related_name="sub_cat")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "物品类别"
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
    需求紧急度
    """
    EMERGENCY_TYPE = (
        (1, "不紧急"),
        (2, "比较紧急"),
        (3, "十万火急"),
    )


    property_type = models.IntegerField(choices=PROPERTY_TYPE, verbose_name="物品属性", help_text="物品是需求条目还是提供条目(1:需求 2:提供)")
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="物品类别")
    emergency = models.IntegerField(choices=EMERGENCY_TYPE, verbose_name="紧急度", help_text="紧急度(only 需求)")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="物品唯一编号")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"用户")
    name = models.CharField(max_length=100, verbose_name="物品名")
    goods_brief = models.TextField(max_length=500, verbose_name="物品简短描述")
    goods_desc = richTextField(verbose_name="物品详细描述", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '物品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


