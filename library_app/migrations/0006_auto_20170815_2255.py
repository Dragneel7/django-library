# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0005_auto_20141229_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('identity', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('lend_from', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Publisher',
            new_name='Company',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='lend_by',
        ),
        migrations.RemoveField(
            model_name='book',
            name='lend_period',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='quotationfrombook',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.RemoveField(
            model_name='quotationfrombook',
            name='user',
        ),
        migrations.DeleteModel(
            name='QuotationFromBook',
        ),
        migrations.AddField(
            model_name='equipment',
            name='company',
            field=models.ForeignKey(to='library_app.Company'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='lend_by',
            field=models.ForeignKey(blank=True, to='library_app.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='lend_period',
            field=models.ForeignKey(to='library_app.LendPeriods'),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'get_latest_by': 'name', 'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
    ]
