# Generated by Django 4.2 on 2023-05-11 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport_matches', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name': 'Матч', 'verbose_name_plural': 'Матчи'},
        ),
        migrations.AlterModelOptions(
            name='sporttype',
            options={'verbose_name': 'Спорт', 'verbose_name_plural': 'Спорт'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Команда', 'verbose_name_plural': 'Команды'},
        ),
        migrations.AlterModelOptions(
            name='tournament',
            options={'verbose_name': 'Турнир', 'verbose_name_plural': 'Турниры'},
        ),
        migrations.AddField(
            model_name='match',
            name='sport_type_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sport_matches.sporttype'),
        ),
        migrations.AddField(
            model_name='match',
            name='sport_type_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sport_matches.sporttype'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sport_matches.tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sport_matches.tournament'),
        ),
        migrations.AddField(
            model_name='sporttype',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sporttype',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='country_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='country_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='gender_en',
            field=models.CharField(blank=True, choices=[('м', 'Мужской'), ('ж', 'Женский')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='gender_ru',
            field=models.CharField(blank=True, choices=[('м', 'Мужской'), ('ж', 'Женский')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='name_en',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='name_ru',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='sport_type_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sport_matches.sporttype'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='sport_type_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sport_matches.sporttype'),
        ),
    ]