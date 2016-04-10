# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app123', '0002_stuff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='photo',
            field=models.ImageField(upload_to=b''),
        ),
    ]
