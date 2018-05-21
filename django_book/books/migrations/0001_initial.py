# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, null=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('authors', models.ManyToManyField(to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=60)),
                ('state_province', models.CharField(blank=True, verbose_name='省名', max_length=30)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, blank=True, to='books.Publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='au_books',
            field=models.ForeignKey(null=True, blank=True, to='books.Book'),
        ),
    ]
