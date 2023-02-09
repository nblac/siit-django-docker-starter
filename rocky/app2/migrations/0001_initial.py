# Generated by Django 4.1.4 on 2023-02-09 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intrebare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('punctaj', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='VariantaRaspuns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corect', models.BooleanField(default=False)),
                ('feedback', models.CharField(blank=True, max_length=50, null=True)),
                ('intrebare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.intrebare')),
            ],
        ),
    ]
