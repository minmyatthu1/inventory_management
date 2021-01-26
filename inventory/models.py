# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Buy(models.Model):
    buy_id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey('Inventory', models.CASCADE)
    buy_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'buy'
        unique_together = (('buy_id', 'inventory'),)


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    item_detail = models.CharField(max_length=100)
    operation = models.CharField(db_column='Operation', max_length=5)  # Field name made lowercase.
    price = models.IntegerField()
    comments = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inventory'


class Sell(models.Model):
    sell_id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey(Inventory, models.CASCADE)
    sell_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sell'
        unique_together = (('sell_id', 'inventory'),)
