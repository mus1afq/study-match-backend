# Generated by Django 4.2 on 2023-05-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studymatch', '0003_groupusers_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
