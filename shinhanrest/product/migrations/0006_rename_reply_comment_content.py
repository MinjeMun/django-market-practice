# Generated by Django 4.1.5 on 2023-01-25 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_user_comment_member_rename_user_like_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reply',
            new_name='content',
        ),
    ]
