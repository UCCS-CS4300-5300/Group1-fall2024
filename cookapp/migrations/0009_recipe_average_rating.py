# Generated by Django 5.1.1 on 2024-11-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0008_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='average_rating',
            field=models.FloatField(default=0.0),
        ),
    ]
