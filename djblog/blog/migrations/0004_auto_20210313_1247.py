# Generated by Django 3.1.7 on 2021-03-13 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210313_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_date',
            new_name='date_created',
        ),
    ]
