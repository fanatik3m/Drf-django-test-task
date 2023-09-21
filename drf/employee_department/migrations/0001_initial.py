# Generated by Django 3.2.9 on 2023-09-17 09:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('last_name', models.CharField(db_index=True, max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(60)])),
                ('emp_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_department.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee_department.employee'),
        ),
    ]
