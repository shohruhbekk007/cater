# Generated by Django 4.0 on 2024-03-29 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sahifa', '0004_alter_event_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='corusel',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='statiska',
            options={'ordering': ['id']},
        ),
    ]
