# Generated by Django 2.2.7 on 2019-11-07 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='eno',
            field=models.CharField(max_length=10),
        ),
    ]
