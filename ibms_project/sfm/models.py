from __future__ import division, print_function, unicode_literals, absolute_import
from django.db import models


class CostCentre(models.Model):
    costCentre = models.CharField(max_length=6, verbose_name="CostCentre",
                                  help_text="Cost Centre")
    name = models.CharField(max_length=128, null=True, blank=True)

    def __unicode__(self):
        return (self.name and "{0} - {1}".format(self.costCentre, self.name) or
                self.costCentre)


class FinancialYear(models.Model):
    financialYear = models.CharField(max_length=10, primary_key=True)

    def __unicode__(self):
        return unicode(self.pk)

    class meta:
        abstract = True


class SFMMetric(models.Model):
    financialYear = models.ForeignKey(FinancialYear)
    servicePriorityNo = models.CharField(
        max_length=100,
        null=False,
        default="-1")
    metricID = models.TextField(null=True)
    descriptor = models.TextField(null=True)
    example = models.TextField(null=True)

    class Meta:
        unique_together = (('financialYear', 'metricID'), )
        verbose_name = 'SFM Metric'
        verbose_name_plural = 'SFM Metric'

    def __unicode__(self):
        return unicode(self.metricID)


class MeasurementType(models.Model):
    unit = models.CharField(max_length=50, null=False)

    def __unicode__(self):
        return self.unit


class Quarter(models.Model):
    financialYear = models.ForeignKey(FinancialYear)
    quarter = models.IntegerField()
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.financialYear.financialYear + " " + self.description


class MeasurementValue(models.Model):
    quarter = models.ForeignKey(Quarter, verbose_name="Related Quarter")
    sfmMetric = models.ForeignKey(SFMMetric, verbose_name="Related SFMMetric")
    measurementType = models.ForeignKey(MeasurementType,
                                        verbose_name="Related MeasurementType",
                                        null=True, blank=True)
    costCentre = models.ForeignKey(CostCentre,
                                   verbose_name="Related Cost Centre")
    value = models.FloatField(null=True, blank=True)
    comment = models.TextField(null=True)

    def __unicode__(self):
        return unicode(self.pk)


class Outcomes(models.Model):
    costCentre = models.ForeignKey(CostCentre)
    comment = models.TextField(null=False)

    class Meta:
        verbose_name_plural = 'outcomes'

    def __unicode__(self):
        return unicode(self.comment)
