# Generated by Django 3.2.13 on 2023-09-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiences', models.CharField(max_length=50)),
                ('where', models.CharField(max_length=50)),
                ('with_who', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('M', 'Mundial'), ('I', 'Internacional'), ('N', 'Nacional')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Idolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=50)),
                ('titles_won', models.CharField(max_length=70)),
                ('games', models.CharField(max_length=20)),
                ('era', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campeonato', models.CharField(max_length=50)),
                ('quantidade', models.CharField(max_length=50)),
            ],
        ),
    ]