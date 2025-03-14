# Generated by Django 5.1.6 on 2025-03-09 06:26

import autoslug.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
                ('name', models.CharField(max_length=64, verbose_name='Currency Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('code', models.CharField(max_length=8, verbose_name='Currency Code')),
                ('code3', models.CharField(blank=True, max_length=8, null=True, verbose_name='Currency Code 3')),
                ('symbol', models.CharField(blank=True, max_length=8, null=True, verbose_name='Currency Symbol')),
                ('order', models.PositiveIntegerField(verbose_name='Currency Order')),
                ('currency_type', models.CharField(choices=[('fiat', 'Fiat Currency'), ('crypto', 'Crypto Currency')], default='fiat', max_length=24, verbose_name='Currency Type')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
                'ordering': ('enabled', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Tokenizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This field is automatically determined by the system, do not interfere.', unique=True, verbose_name='Unique ID')),
                ('uidb64', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Tokenizer',
                'verbose_name_plural': 'Tokenizer',
            },
        ),
    ]
