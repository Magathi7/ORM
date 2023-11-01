# Generated by Django 4.2.6 on 2023-10-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='footballplayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('players_id', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('members', models.CharField(max_length=20)),
            ],
        ),
    ]
