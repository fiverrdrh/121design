# Generated by Django 4.2.6 on 2023-10-09 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'db_table': 'agreement',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('telephone_one', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone_two', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='DailyWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('company_name', models.CharField(blank=True, max_length=500, null=True)),
                ('invoice_number', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'daily_work',
            },
        ),
        migrations.CreateModel(
            name='RefferBy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reffer_by',
            },
        ),
        migrations.CreateModel(
            name='SubContractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('business_name', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('trade_names', models.TextField(blank=True, null=True)),
                ('license_no', models.TextField(blank=True, null=True)),
                ('telephone_one', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone_two', models.CharField(blank=True, max_length=255, null=True)),
                ('email_one', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_two', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'sub_contractor',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('ssn', models.CharField(blank=True, max_length=10, null=True)),
                ('dl_image_front', models.TextField(blank=True, null=True)),
                ('dl_image_back', models.TextField(blank=True, null=True)),
                ('per_day_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('reffer_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.refferby')),
            ],
            options={
                'db_table': 'worker',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('scope_of_works', models.TextField(blank=True, null=True)),
                ('profile_image', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.customer')),
                ('superintendent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_no', models.TextField(blank=True, null=True)),
                ('date', models.DateField(null=True)),
                ('amount', models.TextField(blank=True, null=True)),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.agreement')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='DailyWorkImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_image', models.TextField(blank=True, null=True)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.dailywork')),
            ],
            options={
                'db_table': 'daily_work_image',
            },
        ),
        migrations.CreateModel(
            name='DailyWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.dailywork')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.worker')),
            ],
            options={
                'db_table': 'daily_worker',
            },
        ),
        migrations.AddField(
            model_name='dailywork',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.project'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.project'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='sub_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
