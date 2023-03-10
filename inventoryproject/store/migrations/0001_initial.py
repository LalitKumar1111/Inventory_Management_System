# Generated by Django 4.0.5 on 2022-06-04 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=120, unique=True)),
                ('catdetails', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(max_length=120, unique=True)),
                ('email', models.CharField(max_length=220)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('pcode', models.CharField(max_length=120, unique=True)),
                ('pricepu', models.IntegerField()),
                ('stockinhand', models.IntegerField()),
                ('minstacktomaintain', models.IntegerField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=220)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=220)),
                ('mobile', models.IntegerField()),
                ('depart', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.dept')),
            ],
        ),
        migrations.CreateModel(
            name='SO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sonum', models.CharField(max_length=120, unique=True)),
                ('sodate', models.DateField(null=True)),
                ('rquantity', models.IntegerField()),
                ('priceperunit', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('deliverystatus', models.CharField(choices=[('Delivered', 'Delivered'), ('Undelivered', 'Undelivered')], max_length=20, null=True)),
                ('deptname', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.dept')),
                ('pname', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('uname', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.unit')),
                ('username', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.users')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.unit'),
        ),
        migrations.CreateModel(
            name='PO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponum', models.CharField(max_length=120, unique=True)),
                ('podate', models.DateField(null=True)),
                ('rquantity', models.IntegerField()),
                ('priceperunit', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('deliverystatus', models.CharField(choices=[('Delivered', 'Delivered'), ('Undelivered', 'Undelivered')], max_length=30, null=True)),
                ('paymentstatus', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=30, null=True)),
                ('pname', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('supplier', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.supplier')),
                ('uname', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.unit')),
            ],
        ),
    ]
