# Generated by Django 3.2.13 on 2023-08-04 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='state',
            new_name='estado',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='title',
        ),
        migrations.AddField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(default='***', max_length=256),
        ),
    ]
