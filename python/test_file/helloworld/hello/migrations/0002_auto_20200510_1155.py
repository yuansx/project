# Generated by Django 3.0.6 on 2020-05-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='id',
            field=models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]