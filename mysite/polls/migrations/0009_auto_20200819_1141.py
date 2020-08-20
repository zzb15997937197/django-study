# Generated by Django 2.0 on 2020-08-19 11:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200817_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=180, null=True, verbose_name='描述')),
                ('enabled', models.BooleanField(default=True, verbose_name='有效')),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
                ('delete_datetime', models.DateTimeField(blank=True, null=True, verbose_name='删除时间')),
                ('feedback_content', models.TextField(verbose_name='反馈内容')),
                ('feedback_class', models.IntegerField(verbose_name='反馈类型')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Student', verbose_name='学生id')),
            ],
            options={
                'verbose_name': '学生反馈表',
                'verbose_name_plural': '学生反馈表',
                'db_table': 'student_feedback',
            },
        ),
        migrations.CreateModel(
            name='FeedBackType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=180, null=True, verbose_name='描述')),
                ('enabled', models.BooleanField(default=True, verbose_name='有效')),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
                ('delete_datetime', models.DateTimeField(blank=True, null=True, verbose_name='删除时间')),
                ('name', models.CharField(max_length=50, verbose_name='类型名称')),
            ],
            options={
                'verbose_name': '学生反馈类型表',
                'verbose_name_plural': '学生反馈类型表',
                'db_table': 'student_feedback_type',
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='polls.FeedBackType', verbose_name='类型id'),
        ),
    ]