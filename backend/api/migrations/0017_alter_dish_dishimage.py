# Generated by Django 3.2 on 2023-07-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_dish_dishimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='DishImage',
            field=models.ImageField(default='media/1.png', upload_to='uploads/'),
        ),
    ]
