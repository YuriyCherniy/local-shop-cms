# Generated by Django 2.2.13 on 2020-06-15 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0056_auto_20200512_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='market',
            field=models.URLField(blank=True, help_text='Оставьте поле пустым, чтобы не отображать ссылку в футере.', verbose_name='профиль на торговой площадке ("Юла", "Avito" и т.д.).'),
        ),
    ]
