# Generated by Django 4.2.16 on 2024-12-03 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_rename_comment_comment_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='deployed_site',
        ),
        migrations.RemoveField(
            model_name='project',
            name='repository',
        ),
        migrations.RemoveField(
            model_name='project',
            name='technologies',
        ),
    ]