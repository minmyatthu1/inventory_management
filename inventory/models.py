from django.utils import timezone
from django.db import models


class Buy(models.Model):
    buy_id = models.AutoField(primary_key=True)
    inventory= models.ForeignKey('Inventory', models.CASCADE)
    buy_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'buy'
        unique_together = (('buy_id', 'inventory'),)


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    item_detail = models.CharField(max_length=100)
    # Field name made lowercase.
    status = models.CharField(db_column='Operation', max_length=5)
    price = models.IntegerField()
    comments = models.CharField(max_length=45, blank=True, null=True)
    created_time = models.DateField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'inventory'

    def __str__(self):
        return f"{self.inventory_id}, {self.item_detail}, {self.price}, {self.status}"


class Sell(models.Model):
    sell_id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey(Inventory, models.CASCADE)
    sell_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sell'
        unique_together = (('sell_id', 'inventory'),)
    
    def __str__(self):
        return f"{self.sell_id}, {self.sell_date}" 

# def update_inventory(sender, instance, **kwargs):
#     print("updated")
#     b = Inventory.objects.get(pk=1)
#     b.status = "Sold"
#     b.save()                # update inventory status when signal come


# post_save.connect(update_inventory, sender=Sell)
