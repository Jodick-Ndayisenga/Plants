# Generated by Django 4.2.3 on 2023-12-01 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('preview', models.ImageField(upload_to='static/images')),
                ('comments', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Picinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_sizes', models.TextField(max_length=360)),
                ('captured_time', models.DateField()),
                ('price', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Potato.picture')),
            ],
        ),
    ]
