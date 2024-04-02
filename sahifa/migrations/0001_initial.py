# Generated by Django 4.0 on 2024-03-29 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biz_haqimizda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nomi', models.CharField(max_length=65)),
                ('komment', models.CharField(max_length=255)),
                ('Rasm', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Corusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nomi', models.CharField(max_length=68)),
                ('Haqida', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statiska',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soni', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tadbir_lavhalari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nomi', models.CharField(max_length=60)),
                ('Rasmlar', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Toifalash1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CoruselRu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nomi', models.CharField(max_length=68)),
                ('Haqida', models.CharField(max_length=255)),
                ('carousel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='corusel_ru', to='sahifa.corusel')),
            ],
        ),
        migrations.AddField(
            model_name='corusel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sahifa.toifalash1'),
        ),
    ]
