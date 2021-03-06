# Generated by Django 2.2.9 on 2020-01-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0043_auto_20200112_1110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['sort_position'], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AlterField(
            model_name='item',
            name='sort_position',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, 'нет')], default=10, help_text='Выберете позицию товара на главной (от 1 до 9).', verbose_name='Позиция на главной'),
        ),
    ]
