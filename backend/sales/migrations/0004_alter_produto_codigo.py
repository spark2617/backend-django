# Generated by Django 5.0.6 on 2024-06-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_produto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
