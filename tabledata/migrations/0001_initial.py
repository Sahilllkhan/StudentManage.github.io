# Generated by Django 4.1.3 on 2022-12-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tabledata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('btime', models.CharField(max_length=50)),
                ('photo', models.ImageField(default='', upload_to='static/image')),
                ('fee', models.CharField(max_length=50)),
                ('remfee', models.CharField(max_length=50)),
            ],
        ),
    ]
