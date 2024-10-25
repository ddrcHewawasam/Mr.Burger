# Generated by Django 4.0 on 2024-10-25 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('price', models.FloatField()),
                ('img_url', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.TextField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete')], default='Incomplete', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('delivery_date', models.DateField()),
                ('delivery_time', models.TimeField()),
                ('house_no', models.CharField(max_length=10)),
                ('street1', models.CharField(max_length=255)),
                ('street2', models.CharField(blank=True, max_length=255, null=True)),
                ('town', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webstore.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.order')),
            ],
        ),
    ]