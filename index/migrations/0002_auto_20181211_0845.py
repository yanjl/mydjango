# Generated by Django 2.1.4 on 2018-12-11 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("index", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        )
    ]
