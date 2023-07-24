from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from authentication.models import Profile

class MLMLevelPlan(MPTTModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    direct_income = models.DecimalField(max_digits=10, decimal_places=2)
    level_income = models.DecimalField(max_digits=10, decimal_places=2)
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    sponsor_id = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

class Plans(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    direct_income = models.DecimalField(max_digits=10, decimal_places=2)
    level_income = models.DecimalField(max_digits=10, decimal_places=2)
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    def __str__(self):
        return self.name