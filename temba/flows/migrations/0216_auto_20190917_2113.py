# Generated by Django 2.2.4 on 2019-09-17 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("flows", "0215_auto_20190822_2037")]

    operations = [
        migrations.RemoveField(model_name="flowrun", name="child_context"),
        migrations.RemoveField(model_name="flowrun", name="fields"),
        migrations.RemoveField(model_name="flowrun", name="parent_context"),
    ]
