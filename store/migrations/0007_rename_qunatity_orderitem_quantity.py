# Generated by Django 3.2.7 on 2021-11-06 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_customers_order_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]