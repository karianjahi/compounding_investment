# Generated by Django 5.2.4 on 2025-07-09 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('initial_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentGrowth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('interest', models.DecimalField(decimal_places=2, max_digits=20)),
                ('capital_gains', models.DecimalField(decimal_places=2, max_digits=20)),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wealth_growth', to='grow_your_wealth.investment')),
            ],
            options={
                'ordering': ['year', 'month'],
                'unique_together': {('investment', 'year', 'month')},
            },
        ),
    ]
