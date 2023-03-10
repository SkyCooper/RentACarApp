# Generated by Django 4.1.5 on 2023-01-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0002_remove_car_car_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(choices=[('MRC', 'Mercedes'), ('BMW', 'BMW'), ('AUDI', 'Audi'), ('TYT', 'Toyota'), ('NS', 'Nissan')], max_length=15),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.CharField(choices=[('Diesel ', 'Diesel'), ('Petrol', 'Petrol'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric'), ('LPG', 'LPG')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='gear',
            field=models.CharField(choices=[('Auto', 'Automatic'), ('Manuel', 'Manual')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='rent_per_day',
            field=models.IntegerField(choices=[(1, 250), (2, 500), (3, 800), (4, 1000)]),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.SmallIntegerField(choices=[(2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004)]),
        ),
    ]
