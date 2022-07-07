# Generated by Django 3.2.9 on 2021-11-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('reviews', models.CharField(max_length=40, null=True)),
                ('rates', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
