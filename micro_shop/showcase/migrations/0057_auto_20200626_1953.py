# Generated by Django 2.2.13 on 2020-06-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0056_auto_20200615_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, help_text='Длинна описания не должна превышать 500 символов.', max_length=500, verbose_name='описание'),
        ),
    ]