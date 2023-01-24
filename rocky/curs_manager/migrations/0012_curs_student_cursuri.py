# Generated by Django 4.1.4 on 2023-01-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs_manager', '0011_studentprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=20)),
                ('an', models.IntegerField()),
                ('profesor', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='cursuri',
            field=models.ManyToManyField(to='curs_manager.curs'),
        ),
    ]