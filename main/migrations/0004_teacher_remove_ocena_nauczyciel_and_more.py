# Generated by Django 5.0.6 on 2024-06-10 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_uczen_klasa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='ocena',
            name='nauczyciel',
        ),
        migrations.RemoveField(
            model_name='ocena',
            name='przedmiot',
        ),
        migrations.RemoveField(
            model_name='ocena',
            name='uczen',
        ),
        migrations.RemoveField(
            model_name='uczen',
            name='klasa',
        ),
        migrations.RenameModel(
            old_name='Klasa',
            new_name='SClass',
        ),
        migrations.RenameField(
            model_name='sclass',
            old_name='profil',
            new_name='profile',
        ),
        migrations.RenameModel(
            old_name='Przedmiot',
            new_name='Subject',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='nazwa',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='sclass',
            name='wychowawca',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('address', models.CharField(max_length=255)),
                ('sclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.sclass')),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subject')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='sclass',
            name='teacher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='main.teacher'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Nauczyciel',
        ),
        migrations.DeleteModel(
            name='Ocena',
        ),
        migrations.DeleteModel(
            name='Uczen',
        ),
    ]
