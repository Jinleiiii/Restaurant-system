# Generated by Django 3.2 on 2023-07-10 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230708_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='DishForeignID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.dish'),
        ),
    ]
