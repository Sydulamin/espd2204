# Generated by Django 4.1.3 on 2023-01-26 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('P_price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('pic', models.ImageField(null=True, upload_to='productPIC')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.category')),
            ],
        ),
    ]