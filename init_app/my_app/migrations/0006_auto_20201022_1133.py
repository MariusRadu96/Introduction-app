# Generated by Django 3.1.2 on 2020-10-22 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_auto_20201022_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livegame',
            name='vendor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.vendor'),
        ),
        migrations.AlterField(
            model_name='slotgame',
            name='vendor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.vendor'),
        ),
    ]
