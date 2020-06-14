# coding: utf-8
from django.db import models

# 数据库类型选择
CHOISE_DATABASE = [
    (1, 'PaaS'),
    (2, '收单'),
    (3, '互联网'),
    (4, '金盈信'),
    (5, '风控'),
    (6, '反洗钱')
]

# 操作类型选择
TYP_CHOISE = [
    (1, '数据执行'),
    (2, '数据提取')
]

# 状态选择
STATUS_CHOISE = [
    (1, '未提交'),
    (2, '未审核'),
    (3, '审核一通过'),
    (4, '审核二通过'),
    (5, '已执行'),
    (6, '已驳回')
]

# 用户类型选择
USER_CHOISE = [
    (1, '研发'),
    (2, '审计'),
    (3, 'DBA')
]


# 工单表
class Issue(models.Model):
    issue_id = models.CharField('单号', max_length=20)
    title = models.CharField('标题', max_length=50)
    system = models.IntegerField('系统', choices=CHOISE_DATABASE, default=1)
    typ = models.IntegerField('类型', choices=TYP_CHOISE, default=1)
    content = models.TextField('内容', max_length=200)
    sender = models.CharField('发送人', max_length=20)
    send_time = models.DateTimeField('提交时间', null=True, auto_now_add=True)
    auditors = models.CharField('审核人', max_length=20, null=True, blank=True)
    audit_time = models.DateTimeField('审核时间', null=True, blank=True)
    handler = models.CharField('处理人', max_length=20, null=True, blank=True)
    handle_time = models.DateTimeField('处理时间', null=True, blank=True)
    status = models.IntegerField('工单状态', choices=STATUS_CHOISE, default=1)
    comment = models.TextField('说明', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = '工单表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.issue_id
