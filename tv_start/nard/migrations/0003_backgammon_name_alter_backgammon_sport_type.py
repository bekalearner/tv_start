# Generated by Django 4.2 on 2023-05-15 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nard', '0002_alter_backgammon_options_alter_sporttype_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgammon',
            name='name',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='backgammon',
            name='sport_type',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='nard.sporttype'),
        ),
    ]
