# Generated by Django 2.2.9 on 2020-01-11 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0033_auto_20200111_1956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-pub_date'], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='sort_position',
        ),
    ]
