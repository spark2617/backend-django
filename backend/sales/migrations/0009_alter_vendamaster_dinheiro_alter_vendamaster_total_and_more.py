# Generated by Django 5.0.6 on 2024-06-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_alter_vendamaster_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendamaster',
            name='dinheiro',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vendamaster',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vendamaster',
            name='troco',
            field=models.IntegerField(default=0),
        ),
    ]
