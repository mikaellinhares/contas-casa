# Generated by Django 5.0.4 on 2024-05-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0003_propriedade_descricao_propriedade_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propriedade',
            name='imagem',
            field=models.ImageField(null=True, upload_to='propriedades'),
        ),
    ]