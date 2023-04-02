# Generated by Django 4.1.7 on 2023-03-10 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('synopsis', models.TextField()),
                ('air_date', models.DateField()),
                ('image', models.ImageField(upload_to='media/episodes')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='season.season')),
            ],
        ),
    ]
