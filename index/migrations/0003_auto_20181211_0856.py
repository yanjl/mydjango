# Generated by Django 2.1.4 on 2018-12-11 00:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [("index", "0002_auto_20181211_0845")]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        )
    ]
