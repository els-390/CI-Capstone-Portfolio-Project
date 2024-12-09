# Generated by Django 4.2.16 on 2024-12-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_deployed_site_project_repository_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deployed_site',
            field=models.URLField(default='https://default.com', verbose_name='Deployed Link'),
        ),
        migrations.AlterField(
            model_name='project',
            name='repository',
            field=models.URLField(default='https://default.com', verbose_name='GitHub Link'),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.TextField(default='placeholder', verbose_name='Technologies'),
        ),
    ]