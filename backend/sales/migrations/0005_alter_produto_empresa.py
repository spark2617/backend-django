# Generated by Django 5.0.6 on 2024-06-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_produto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='empresa',
            field=models.CharField(max_length=100, null=True),
        ),
    ]