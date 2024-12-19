# Generated by Django 5.1.2 on 2024-12-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialist_in', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_joining', models.DateField()),
                ('years_experience', models.PositiveIntegerField()),
                ('study', models.TextField()),
                ('image', models.ImageField(upload_to='doctors/images/')),
            ],
        ),
    ]
