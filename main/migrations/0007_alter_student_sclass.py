# Generated by Django 5.0.6 on 2024-06-20 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_userconnect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sclass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.sclass'),
            preserve_default=False,
        ),
    ]
