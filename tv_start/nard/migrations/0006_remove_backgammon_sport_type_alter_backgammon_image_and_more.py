# Generated by Django 4.2 on 2023-05-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nard', '0005_alter_backgammon_image_alter_backgammon_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backgammon',
            name='sport_type',
        ),
        migrations.AlterField(
            model_name='backgammon',
            name='image',
            field=models.ImageField(default='nard_images/nardy-youtube-13_03_23-600x350.jpg', null=True, upload_to='nard_images/'),
        ),
        migrations.DeleteModel(
            name='SportType',
        ),
    ]