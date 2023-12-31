# Generated by Django 3.2.22 on 2023-10-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_description', models.TextField()),
                ('bug_type', models.CharField(choices=[('error', 'error'), ('new features', 'new features'), ('new deployment', 'new deployment')], max_length=50)),
                ('bug_report_date', models.DateField()),
                ('bug_status', models.CharField(choices=[('Done', 'Done'), ('TO do', 'TO do'), ('In progress', 'In progress'), ('Almost Done', 'Almost Done')], max_length=50)),
            ],
        ),
    ]
