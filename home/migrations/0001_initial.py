# Generated by Django 3.1.1 on 2020-09-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('serial_number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('content', models.TextField()),
                ('email', models.CharField(max_length=70)),
            ],
        ),
    ]