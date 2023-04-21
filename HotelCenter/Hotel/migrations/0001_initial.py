# Generated by Django 4.0.3 on 2023-04-21 12:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=70)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('floor_count', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(max_length=55)),
                ('city', models.CharField(max_length=55)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('check_in', models.TimeField(blank=True, null=True)),
                ('check_out', models.TimeField(blank=True, null=True)),
                ('rate', models.FloatField(default=2.5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HotelManager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-rate'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default=None, max_length=100)),
                ('size', models.IntegerField(default=0)),
                ('view', models.CharField(default=None, max_length=100)),
                ('sleeps', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('option', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='roomFacility',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='roomImages')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(related_name='rooms', to='Hotel.roomfacility'),
        ),
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='Hotel.hotel'),
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('adults', models.IntegerField(default=None)),
                ('children', models.IntegerField(default=None)),
                ('total_price', models.IntegerField(default=None)),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('phone_number', models.CharField(blank=True, max_length=64, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reserves', to='Hotel.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hotel')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='images', to='Hotel.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='Hotel.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CancelReserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('price_per_day', models.IntegerField(default=None)),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('national_code', models.CharField(blank=True, max_length=64, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=64, null=True)),
                ('reserve', models.IntegerField()),
                ('canceld_at', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Hotel.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
