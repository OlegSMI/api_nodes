# Generated by Django 3.2.11 on 2022-01-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_note_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
