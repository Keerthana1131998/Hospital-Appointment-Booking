# Generated by Django 5.0 on 2024-02-17 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_remove_register_table_otp_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_table',
            old_name='Appointment_time',
            new_name='appointment_time',
        ),
        migrations.RenameField(
            model_name='register_table',
            old_name='Reason_for_the_appointment',
            new_name='reason_for_the_appointment',
        ),
    ]
