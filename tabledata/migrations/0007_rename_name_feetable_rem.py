# Generated by Django 4.1.3 on 2022-12-15 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabledata', '0006_feetable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feetable',
            old_name='name',
            new_name='rem',
        ),
    ]