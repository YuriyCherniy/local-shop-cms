# Generated by Django 2.2.9 on 2019-12-19 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0020_auto_20191219_1331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-pub_date'], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
    ]
