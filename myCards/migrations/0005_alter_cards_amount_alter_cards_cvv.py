# Generated by Django 4.2.5 on 2023-10-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCards', '0004_alter_cards_card_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='amount',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cards',
            name='cvv',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
