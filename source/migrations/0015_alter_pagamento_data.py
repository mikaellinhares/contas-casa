# Generated by Django 5.0.4 on 2024-09-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0014_parcelamento_despesa_parcelamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='data',
            field=models.DateField(),
        ),
    ]
