# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newyear', '0003_auto_20191229_1001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '会员', 'verbose_name_plural': '会员'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(verbose_name='联系电话', max_length=11, unique=True),
        ),
    ]
