# Generated by Django 4.1.2 on 2022-12-04 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_projects_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='task',
        ),
        migrations.AddField(
            model_name='doings',
            name='task',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='doings', to='webapp.projects', verbose_name='Задача'),
            preserve_default=False,
        ),
    ]
