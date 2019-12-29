# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newyear', '0004_auto_20191229_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='desc',
            field=models.CharField(verbose_name='说明', max_length=50, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='is_win',
            field=models.BooleanField(verbose_name='是否中奖', default=False),
        ),
    ]
