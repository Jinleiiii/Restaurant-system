# Generated by Django 3.2 on 2023-07-24 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_dish_costtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('DishID', models.IntegerField(primary_key=True, serialize=False)),
                ('DishAmount', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='CompleteStatus',
            field=models.IntegerField(choices=[(0, 'Not taking the order'), (1, 'Dish completed, waiting for serving'), (2, 'Serving completed')], default=0),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='DishID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dish'),
        ),
    ]
