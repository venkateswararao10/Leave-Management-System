# Generated by Django 5.0 on 2024-01-09 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0008_rename_applied_year_leaves_year'),
        ('registration', '0004_remove_faculty_section_id_delete_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaves',
            name='dept_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.department'),
        ),
    ]
