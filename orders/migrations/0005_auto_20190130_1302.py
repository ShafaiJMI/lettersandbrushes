# Generated by Django 2.1.4 on 2019-01-30 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190129_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',)},
        ),
        migrations.RemoveField(
            model_name='order',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order'),
        ),
    ]
