# Generated by Django 5.0.6 on 2024-06-10 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uczen',
            old_name='klasa_F',
            new_name='klasa',
        ),
    ]
