# Generated by Django 4.0.4 on 2022-06-20 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0008_rename_name_marcas_marcas_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ropa',
            old_name='marcas_name',
            new_name='ropa_marca',
        ),
    ]