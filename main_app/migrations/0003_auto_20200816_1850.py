# Generated by Django 3.0.8 on 2020-08-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_f1_f2'),
    ]

    operations = [
        migrations.AddField(
            model_name='f1',
            name='trips',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='f1',
            name='bags',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='f1',
            name='vehicle',
            field=models.IntegerField(blank=True),
        ),
    ]
