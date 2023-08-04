# Generated by Django 3.2 on 2023-06-25 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryID', models.AutoField(primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('DishID', models.AutoField(primary_key=True, serialize=False)),
                ('DishName', models.CharField(max_length=20)),
                ('Price', models.FloatField(default=0)),
                ('Description', models.CharField(max_length=50)),
                ('Ingredients', models.CharField(max_length=50)),
                ('DishType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.category')),
            ],
        ),
    ]
