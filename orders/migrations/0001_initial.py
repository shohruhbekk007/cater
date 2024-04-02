# Generated by Django 4.0 on 2024-03-29 07:46

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pasuda_qoshish', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('product', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pasuda_qoshish.maxsulot')),
            ],
            managers=[
                ('orders', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('category_name', models.CharField(blank=True, max_length=255)),
            ],
            managers=[
                ('sales', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_admin', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='user_groups', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_permissions', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SaleRu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=255)),
                ('sale', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sotuv_ru', to='orders.sale')),
            ],
        ),
        migrations.CreateModel(
            name='OrderRu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_ru', to='orders.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.sale'),
        ),
    ]
