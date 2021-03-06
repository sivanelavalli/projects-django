# Generated by Django 2.1.5 on 2019-01-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('doj', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=20)),
                ('contactno', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
