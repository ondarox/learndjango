# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app123', '0007_auto_20160331_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutstuff',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='aboutstuff',
            name='reviewtext',
        ),
        migrations.AddField(
            model_name='aboutstuff',
            name='aboutheading',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutstuff',
            name='abouttext',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutstuff',
            name='stuff',
            field=models.OneToOneField(null=True, to='app123.Stuff'),
        ),
    ]
