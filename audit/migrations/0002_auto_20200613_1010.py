# Generated by Django 3.0 on 2020-06-13 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='auditors',
            field=models.CharField(max_length=20, verbose_name='审核人'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='handler',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='处理人'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='提交时间'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='sender',
            field=models.CharField(max_length=20, verbose_name='发送人'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.IntegerField(choices=[('1', '未提交'), ('2', '未审核'), ('3', '审核一通过'), ('4', '审核二通过'), ('5', '已执行'), ('6', '已驳回')], default='1', verbose_name='工单状态'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='typ',
            field=models.IntegerField(choices=[('1', '数据执行'), ('2', '数据提取')], default='1', verbose_name='类型'),
        ),
    ]
