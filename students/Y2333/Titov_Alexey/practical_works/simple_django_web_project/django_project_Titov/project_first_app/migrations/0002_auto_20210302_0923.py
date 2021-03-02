# Generated by Django 3.1.7 on 2021-03-02 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('issue_date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.owner')),
            ],
        ),
        migrations.CreateModel(
            name='CarOwning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.owner')),
            ],
        ),
    ]