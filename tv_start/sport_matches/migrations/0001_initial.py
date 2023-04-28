# Generated by Django 4.2 on 2023-04-28 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('logo', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('gender', models.CharField(blank=True, choices=[('м', 'Мужской'), ('ж', 'Женский')], max_length=1)),
                ('sport_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sport_matches.sporttype')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('sport_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_matches.sporttype')),
                ('team_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_one', to='sport_matches.team')),
                ('team_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_two', to='sport_matches.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_matches.tournament')),
            ],
        ),
    ]