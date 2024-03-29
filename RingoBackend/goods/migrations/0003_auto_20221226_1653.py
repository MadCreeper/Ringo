# Generated by Django 3.2 on 2022-12-26 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_goods_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='property_type',
            field=models.IntegerField(choices=[(0, '需求物品'), (1, '提供物品')], help_text='物品是需求条目还是提供条目(0:需求 1:提供)', verbose_name='物品属性'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.goodscategory', verbose_name='父类目'),
        ),
    ]
