# Generated by Django 3.2 on 2021-04-24 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_alter_people_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='panel.category'),
            preserve_default=False,
        ),
    ]