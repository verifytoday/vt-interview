# Generated by Django 4.2.11 on 2024-04-03 21:09

from django.db import migrations, models


def create_additional_interview_data(apps, schema_editor):
    Payroll = apps.get_model('accounts', 'Payroll')
    # Create Additional Payroll objects
    Payroll.objects.create(
        account_id=2,
        check_date='2024-03-29',
        pay_start='2024-03-10',
        pay_end='2024-03-23',
        gross_hours=80.0,
        base_wages=1000.0,
        gross_wages=1000.0,
        employee_first_name='Amy',
        employee_last_name='Masters',
    )
    Payroll.objects.create(
        account_id=2,
        check_date='2024-03-29',
        pay_start='2024-03-10',
        pay_end='2024-03-23',
        gross_hours=80.0,
        base_wages=1000.0,
        gross_wages=1000.0,
        employee_first_name='Emily',
        employee_last_name='Joseph',
    )

    check_dates_list = [
        ['2024-01-01', '2024-01-15', '2024-01-16'],
        ['2024-01-16', '2024-01-31', '2024-02-01'],
        ['2024-02-01', '2024-02-15', '2024-02-16'],
        ['2024-02-16', '2024-02-29', '2024-03-01'],
        ['2024-03-01', '2024-03-15', '2024-03-16'],
        ['2024-03-16', '2024-03-31', '2024-04-01']
    ]

    employees = [
        ['Laura', 'Jacobs'],
        ['Anne', 'Hill'],
        ['Jennifer', 'Gribble'],
        ['Teresa', 'Scott'],
        ['Maegan', 'Barb'],
        ['Beatrice', 'Wood'],
        ['Mary', 'Arthouse'],
        ['Audrey', 'Smith']
    ]

    for check_date in check_dates_list:
        for employee in employees:
            Payroll.objects.create(
                account_id=2,
                check_date=check_date[2],
                pay_start=check_date[0],
                pay_end=check_date[1],
                gross_hours=80.0,
                base_wages=1000.0,
                gross_wages=1000.0,
                employee_first_name=employee[0],
                employee_last_name=employee[1],
            )


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_create_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='employee_first_name',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payroll',
            name='employee_last_name',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='name',
            field=models.CharField(choices=[('Client', 'Client'), ('Partner', 'Partner')], max_length=255),
        ),
        migrations.RunPython(create_additional_interview_data)
    ]
