# Generated by Django 4.2 on 2023-05-12 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_matches', '0007_alter_match_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='img',
            new_name='image',
        ),
    ]
