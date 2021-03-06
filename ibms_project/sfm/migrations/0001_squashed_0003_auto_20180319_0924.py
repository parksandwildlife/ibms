# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-19 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('sfm', '0001_initial'), ('sfm', '0002_auto_20150811_1031'), ('sfm', '0003_auto_20180319_0924')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostCentre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costCentre', models.CharField(help_text='Cost Centre', max_length=6, verbose_name='CostCentre')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialYear',
            fields=[
                ('financialYear', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, null=True)),
                ('comment', models.TextField(null=True)),
                ('costCentre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sfm.CostCentre', verbose_name='Related Cost Centre')),
                ('measurementType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sfm.MeasurementType', verbose_name='Related MeasurementType')),
            ],
        ),
        migrations.CreateModel(
            name='Outcomes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('costCentre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sfm.CostCentre')),
            ],
            options={
                'verbose_name_plural': 'outcomes',
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('financialYear', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sfm.FinancialYear')),
            ],
        ),
        migrations.CreateModel(
            name='SFMMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financialYear', models.CharField(max_length=10)),
                ('servicePriorityNo', models.CharField(default='-1', max_length=100)),
                ('metricID', models.TextField(null=True)),
                ('descriptor', models.TextField(null=True)),
                ('example', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'SFM Metric',
                'verbose_name_plural': 'SFM Metric',
            },
        ),
        migrations.AlterUniqueTogether(
            name='sfmmetric',
            unique_together=set([('financialYear', 'metricID')]),
        ),
        migrations.AddField(
            model_name='measurementvalue',
            name='quarter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sfm.Quarter', verbose_name='Related Quarter'),
        ),
        migrations.AddField(
            model_name='measurementvalue',
            name='sfmMetric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sfm.SFMMetric', verbose_name='Related SFMMetric'),
        ),
        migrations.AlterField(
            model_name='sfmmetric',
            name='financialYear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sfm.FinancialYear'),
        ),
        migrations.AlterField(
            model_name='measurementvalue',
            name='costCentre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sfm.CostCentre', verbose_name='Related Cost Centre'),
        ),
        migrations.AlterField(
            model_name='measurementvalue',
            name='measurementType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sfm.MeasurementType', verbose_name='Related MeasurementType'),
        ),
        migrations.AlterField(
            model_name='sfmmetric',
            name='financialYear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sfm.FinancialYear'),
        ),
    ]
