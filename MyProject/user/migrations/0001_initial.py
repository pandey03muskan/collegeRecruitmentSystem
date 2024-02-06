# Generated by Django 3.2.4 on 2021-10-04 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applyjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jid', models.IntegerField()),
                ('sid', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=40)),
                ('cpic', models.ImageField(default='', upload_to='static/companies/')),
                ('cdate', models.DateField()),
                ('curl', models.CharField(max_length=500)),
                ('ccity', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('contact', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=200)),
                ('passwd', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('resume', models.ImageField(default='', upload_to='static/resume/')),
                ('picture', models.ImageField(default='', upload_to='static/profile/')),
            ],
        ),
        migrations.CreateModel(
            name='vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jid', models.IntegerField()),
                ('designation', models.CharField(max_length=200)),
                ('vacant', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=200)),
                ('skill', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=100)),
                ('clocation', models.CharField(max_length=40)),
                ('ccompany', models.CharField(max_length=100)),
                ('vdate', models.DateField()),
                ('vpic', models.ImageField(default='', upload_to='static/card/')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.companies')),
            ],
        ),
    ]