# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0066_auto_20170828_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=254, null=True, blank=True)),
                ('ip_address', models.IPAddressField(default=None, null=True, blank=True)),
                ('amount', models.FloatField(default=0)),
                ('city', models.CharField(max_length=254, null=True, blank=True)),
                ('region_code', models.CharField(max_length=10, null=True, blank=True)),
                ('region_name', models.CharField(max_length=254, null=True, blank=True)),
                ('time_zone', models.CharField(max_length=254, null=True, blank=True)),
                ('country_name', models.CharField(max_length=254, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=30, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
