# Generated by Django 3.2 on 2021-04-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_auto_20210424_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='username',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='نام کاربری'),
        ),
    ]
