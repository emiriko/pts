# Generated by Django 4.2.6 on 2023-10-20 10:21

from django.core.management import call_command
from django.db import migrations

def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "books.json")
    
class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]
