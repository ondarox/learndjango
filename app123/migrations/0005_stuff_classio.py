# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app123', '0004_auto_20160304_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='classio',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
