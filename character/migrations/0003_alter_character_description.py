# Generated by Django 4.1.7 on 2023-03-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_alter_character_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
