# Generated by Django 3.2.23 on 2023-12-16 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admision_date', models.DateTimeField(auto_now_add=True)),
                ('discharge_date', models.DateTimeField(null=True)),
                ('diagnosis', models.CharField(max_length=1000)),
                ('treatment', models.CharField(max_length=1000)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doctor.doctorinfo')),
            ],
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('phone_number', models.IntegerField(default=None, null=True, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.CharField(max_length=1000)),
                ('dosage', models.CharField(max_length=1000)),
                ('instruction', models.CharField(max_length=1000)),
                ('MedicalRecord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.medicalrecord')),
            ],
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patientinfo'),
        ),
    ]
