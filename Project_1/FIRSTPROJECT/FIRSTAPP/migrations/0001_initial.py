# Generated by Django 3.2.5 on 2021-07-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subjects', models.IntegerField()),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
    ]