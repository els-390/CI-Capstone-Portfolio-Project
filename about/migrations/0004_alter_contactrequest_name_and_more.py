# Generated by Django 4.2.16 on 2024-12-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_contactrequest_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
