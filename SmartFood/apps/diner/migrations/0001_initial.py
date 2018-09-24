# Generated by Django 2.1.1 on 2018-09-24 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0004_manager'),
        ('user', '0003_auto_20180924_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.FloatField()),
                ('religion', models.CharField(max_length=50)),
                ('nacionality', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('weightKg', models.FloatField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='HealthCharacteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('ingredient', models.ManyToManyField(to='restaurant.Ingredient')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favouriteTypeOfProduct', models.CharField(max_length=50)),
                ('isGlutton', models.BooleanField()),
                ('ingredient', models.ManyToManyField(to='restaurant.Ingredient')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]