# Generated by Django 4.0 on 2024-03-29 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sahifa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('comment', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsRu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('comment', models.CharField(max_length=255)),
                ('about_us', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='about_us_ru', to='sahifa.aboutus')),
            ],
        ),
        migrations.DeleteModel(
            name='Biz_haqimizda',
        ),
    ]
