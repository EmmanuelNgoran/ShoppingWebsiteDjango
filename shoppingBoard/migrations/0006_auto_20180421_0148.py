# Generated by Django 2.0.4 on 2018-04-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingBoard', '0005_auto_20180420_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='address',
            field=models.TextField(max_length=300),
        ),
    ]