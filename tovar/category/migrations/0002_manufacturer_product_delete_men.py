# Generated by Django 4.1.7 on 2023-03-16 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('size', models.TextField()),
                ('manufactur', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='category.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.DeleteModel(
            name='Men',
        ),
    ]
