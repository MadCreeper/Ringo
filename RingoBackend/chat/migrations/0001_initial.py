# Generated by Django 3.2 on 2022-12-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=255, verbose_name='发送用户名')),
                ('to_user', models.CharField(max_length=255, verbose_name='接收用户名')),
                ('room', models.CharField(max_length=255, verbose_name='聊天组号')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='写入时间')),
            ],
        ),
    ]
