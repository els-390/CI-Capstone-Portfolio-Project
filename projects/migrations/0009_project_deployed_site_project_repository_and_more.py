# Generated by Django 4.2.16 on 2024-12-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_remove_project_deployed_site_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deployed_site',
            field=models.URLField(default='https://default.com', verbose_name='url'),
        ),
        migrations.AddField(
            model_name='project',
            name='repository',
            field=models.URLField(default='https://default.com', verbose_name='url'),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.TextField(default='placeholder', verbose_name='html'),
        ),
    ]