# Generated by Django 2.0 on 2020-08-17 14:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200811_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='resourcepackage',
            name='create_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='resourcepackage',
            name='delete_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='删除时间'),
        ),
        migrations.AddField(
            model_name='resourcepackage',
            name='description',
            field=models.CharField(blank=True, default='', max_length=180, null=True, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='resourcepackage',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='有效'),
        ),
        migrations.AddField(
            model_name='resourcepackage',
            name='update_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='student',
            name='create_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='student',
            name='delete_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='删除时间'),
        ),
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.CharField(blank=True, default='', max_length=180, null=True, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='student',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='有效'),
        ),
        migrations.AddField(
            model_name='student',
            name='update_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='polls_custo_last_na_41fb17_idx'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['first_name'], name='first_name_idx'),
        ),
    ]
