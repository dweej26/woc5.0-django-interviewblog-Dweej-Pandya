# Generated by Django 4.1.5 on 2023-02-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_post_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default='draft', max_length=255),
        ),
    ]
