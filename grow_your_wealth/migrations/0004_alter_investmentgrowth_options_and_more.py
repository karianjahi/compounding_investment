# Generated by Django 5.2.4 on 2025-07-09 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grow_your_wealth', '0003_alter_investment_company_alter_investment_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='investmentgrowth',
            options={'ordering': ['year', 'month'], 'verbose_name': 'Investment Growth Record', 'verbose_name_plural': 'Investment Growth Records'},
        ),
        migrations.RenameField(
            model_name='investmentgrowth',
            old_name='capital_gains',
            new_name='updated_capital',
        ),
        migrations.AlterField(
            model_name='investment',
            name='topup_frequency',
            field=models.CharField(default='month', help_text='Defaults to month for now', max_length=20),
        ),
        migrations.AlterField(
            model_name='investmentgrowth',
            name='month',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
    ]
