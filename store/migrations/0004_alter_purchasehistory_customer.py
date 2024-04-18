# Generated by Django 5.0.4 on 2024-04-18 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_purchasehistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasehistory',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
    ]