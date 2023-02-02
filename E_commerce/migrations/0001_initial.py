# Generated by Django 2.2.1 on 2023-02-02 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('brand_store', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10)),
                ('email_address', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_value_of_the_order', models.FloatField()),
                ('purchase_date', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_commerce.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('average_rating', models.FloatField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_commerce.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_date_of_delivery_of_each_product', models.DateTimeField()),
                ('quantity', models.IntegerField(default=1)),
                ('order_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_commerce.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_commerce.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='E_commerce.OrderProduct', to='E_commerce.Product'),
        ),
        migrations.CreateModel(
            name='CostomerPanDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan_number', models.CharField(max_length=13)),
                ('name_of_customer', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('pan_details_are_verified', models.BooleanField(default=False)),
                ('customer_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='E_commerce.Customer')),
            ],
        ),
    ]
