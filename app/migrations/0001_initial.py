# Generated by Django 2.1.3 on 2018-11-14 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('football', 'football'), ('volleyball', 'volleyball'), ('basketball', 'basketball'), ('handball', 'handball'), ('rugby', 'rugby'), ('american football', 'american football'), ('baseball', 'basebal')], max_length=50)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Facility')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sport'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District'),
        ),
    ]
