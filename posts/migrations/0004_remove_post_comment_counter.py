# Generated by Django 3.0.6 on 2020-05-13 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_comment_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_counter',
        ),
    ]
