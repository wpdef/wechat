# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newyear', '0005_auto_20191229_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='desc',
            field=models.CharField(verbose_name='说明', max_length=50, blank=True, null=True),
        ),
    ]
