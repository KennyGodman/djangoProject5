# Generated by Django 4.1.3 on 2022-11-21 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='lasttName',
            new_name='lastName',
        ),
    ]