# Generated by Django 3.0.8 on 2020-07-06 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerid', models.CharField(max_length=100)),
                ('difficulitylevel', models.CharField(max_length=10)),
                ('guessnumber', models.CharField(default='No Record', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]