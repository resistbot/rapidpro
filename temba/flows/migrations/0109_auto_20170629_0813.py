# Generated by Django 1.11.2 on 2017-06-29 08:13

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("flows", "0108_populate_flowrun_uuid")]

    operations = [
        migrations.AlterField(
            model_name="flowrun", name="uuid", field=models.UUIDField(default=uuid.uuid4, unique=True)
        )
    ]
