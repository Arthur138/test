# Generated by Django 4.1.2 on 2022-12-23 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_projects_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doings',
            options={'permissions': [('project_member', 'Участник проекта')]},
        ),
    ]
