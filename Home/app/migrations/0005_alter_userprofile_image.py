# Generated by Django 4.1.3 on 2023-01-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profilePIC'),
        ),
    ]
