"""
Initial migration for the api app.
"""

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Doctor', 'Doctor'), ('Patient', 'Patient')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('availability', models.CharField(choices=[('Available', 'Available'), ('Busy', 'Busy')], max_length=20)),
                ('experience', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_age', models.PositiveIntegerField()),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('UPI', 'UPI')], max_length=20)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending')], max_length=20)),
                ('appointment_status', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Booked', 'Booked'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=20)),
                ('upi_id', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='api.doctor')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
