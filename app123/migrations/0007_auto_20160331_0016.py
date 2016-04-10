# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app123', '0006_comment_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutstuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reviewtext', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to=b'media_review')),
            ],
        ),
        migrations.AddField(
            model_name='stuff',
            name='numb',
            field=models.IntegerField(null=True),
        ),
    ]
