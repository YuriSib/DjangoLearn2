# Generated by Django 5.0.1 on 2024-02-04 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductUsedFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.product')),
                ('used_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.usedfor')),
            ],
        ),
    ]
