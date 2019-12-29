# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newyear', '0002_catetype_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='type',
            field=models.ForeignKey(verbose_name='奖品等级', blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='newyear.cateType'),
        ),
    ]
