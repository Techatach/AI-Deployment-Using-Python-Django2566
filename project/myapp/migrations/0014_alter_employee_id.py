# Generated by Django 4.1.4 on 2023-02-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0013_alter_employee_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]