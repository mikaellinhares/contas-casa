# Generated by Django 5.0.4 on 2024-05-27 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0007_alter_despesa_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='data_criacao',
            field=models.DateField(auto_now_add=True),
        ),
    ]
