# Generated by Django 4.2.2 on 2023-06-16 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichasapp', '0004_ficha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ficha',
            old_name='previcion_salud',
            new_name='prevision_salud',
        ),
    ]
