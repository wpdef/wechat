# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newyear', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catetype',
            name='index',
            field=models.IntegerField(verbose_name='数字越大越靠前', default=1),
            preserve_default=False,
        ),
    ]
