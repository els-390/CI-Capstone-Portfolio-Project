# Generated by Django 4.2.16 on 2024-12-02 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_rename_content_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
    ]