# Generated by Django 5.0 on 2024-01-09 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0006_alter_leaves_applied_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaves',
            name='applied_year',
            field=models.IntegerField(null=True),
        ),
    ]
