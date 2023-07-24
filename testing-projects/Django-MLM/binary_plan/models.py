from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from authentication.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from shortuuid.django_fields import ShortUUIDField

class BinaryUserInstence(MPTTModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_instance')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    refferal = TreeForeignKey ('self', on_delete=models.CASCADE, null=True, blank=True, related_name='refferals')

    left_leg = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='left_legs', default=None)
    right_leg = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='right_legs', default=None)

    #incomes 
    direct_income = models.FloatField(default=0)
    step_income = models.FloatField(default=0)
    binary_income = models.FloatField(default=0)
    gift_and_rewards = models.FloatField(default=0)

    business_volume = models.FloatField(default=0)

    live = models.BooleanField(default=True)

    stage1 = models.BooleanField(default=False)
    stage2 = models.BooleanField(default=False)
    stage3 = models.BooleanField(default=False)
    stage4 = models.BooleanField(default=False)

    number_of_referrals = models.IntegerField(default=0)

    class MPTTMeta:
        order_insertion_by = ['user']

    def count_child_nodes(self):
        left_leg_count = self.left_leg.count_child_nodes() if self.left_leg else 0
        right_leg_count = self.right_leg.count_child_nodes() if self.right_leg else 0

        return 1 + left_leg_count + right_leg_count
    
    def is_live(self):
        return self.live
    
    def update_live(self):
        num_of_referrals = BinaryUserInstence.objects.filter(refferal=self, live=True).count()
        if num_of_referrals >= 2 and self.business_volume >= 0:
            self.live = True
            self.save()
        
    def check_stage_1(self):
        if self.stage1 == False:
            total_active_referrals = BinaryUserInstence.objects.filter(refferal=self, live=True).count()
            if total_active_referrals == 10:
                self.stage1 = True
                self.save()
        return self.stage1
    
    def check_stage_2(self):
        if self.stage2 == False:
            total_active_referrals = BinaryUserInstence.objects.filter(refferal=self, live=True)
            
            for referral in total_active_referrals:
                if referral.stage1 == False:
                    return False

            self.stage2 = True
            self.save()

        return self.stage2

    def check_stage_3(self):
        if self.stage3 == False:
            total_active_referrals = BinaryUserInstence.objects.filter(refferal=self, live=True)
            
            for referral in total_active_referrals:
                if referral.stage2 == False:
                    return False

            self.stage3 = True
            self.save()

        return self.stage3
    
    def check_stage_4(self):
        if self.stage4 == False:
            total_active_referrals = BinaryUserInstence.objects.filter(refferal=self, live=True)
            
            for referral in total_active_referrals:
                if referral.stage3 == False:
                    return False

            self.stage4 = True
            self.save()

        return self.stage4

    def get_left_leg(self):
        return self.left_leg
    
    def get_right_leg(self):
        return self.right_leg
    
    def get_parent(self):
        return self.parent

    def __str__(self):
        return self.user.user_id

class BinaryTreeQueue(models.Model):
    item = models.ForeignKey(BinaryUserInstence, on_delete=models.CASCADE, related_name='user_instance', default=0)

    def enqueue(self, item):
        self.item = item
        self.save()

    def dequeue(self):
        try:
            item = BinaryTreeQueue.objects.earliest('pk')
            item.delete()
            return item.item
        except BinaryTreeQueue.DoesNotExist:
            return None

    def peek(self):
        try:
            return BinaryTreeQueue.objects.earliest('pk').item
        except BinaryTreeQueue.DoesNotExist:
            return None

    def is_empty(self):
        return BinaryTreeQueue.objects.count() == 0 
    
    def __str__(self):
        return self.item.user.user_id
    
# django signal to create user instance after saving profile
@receiver(post_save, sender=Profile)
def create_user(sender, instance, created, **kwargs):
    if created:
        if instance._referral_user_id:
            #Add user instance to referral tree
            instance._referral_user_id.number_of_referrals = instance._referral_user_id.number_of_referrals + 1
            
            #Make user live if its not
            if instance._referral_user_id.is_live() == False:
                instance._referral_user_id.update_live()

            #Calculate step income
            if instance._referral_user_id.check_stage_1():
                instance._referral_user_id.step_income = instance._referral_user_id.direct_income + 100
            
            if instance._referral_user_id.check_stage_2():
                instance._referral_user_id.step_income = instance._referral_user_id.step_income + 100

            if instance._referral_user_id.check_stage_3():
                instance._referral_user_id.step_income = instance._referral_user_id.binary_income + 100
            
            if instance._referral_user_id.check_stage_4():
                instance._referral_user_id.step_income = instance._referral_user_id.gift_and_rewards + 100

            #Calculate binary income

            #Calculate gift and rewards

            instance._referral_user_id.save()
            new_user = BinaryUserInstence.objects.create(user=instance, refferal=instance._referral_user_id)
        else:
            new_user = BinaryUserInstence.objects.create(user=instance)

        #Add user instance to binary tree
        queue_instance = BinaryTreeQueue()
        current = queue_instance.dequeue()
        
        if current.left_leg is None:
            current.left_leg = new_user
            new_user.parent = current
            
        elif current.right_leg is None:
            current.right_leg = new_user
            new_user.parent = current

        current.save()
        new_user.save()
        queue_instance.enqueue(new_user)
        queue_instance.save()
        
        queue_instance2 = BinaryTreeQueue()
        queue_instance2.enqueue(new_user)
        queue_instance2.save()

class BinaryWallet(models.Model):
    TRANSACTION_TYPE = (
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
    )

    INCOME_TYPE = (
        ('direct', 'Direct'),
        ('step', 'Step'),
        ('binary', 'Binary'),
        ('gift_reward', 'Gift_Reward'),
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='binary_wallet')
    balance = models.FloatField(default=0)
    total_income = models.FloatField(default=0)
    total_withdrawn = models.FloatField(default=0)
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.total_withdrawn = self.total_withdrawn + amount
        transaction = TransactionLog.objects.create(wallet=self, amount=amount, transaction_type='withdraw', income_type='nil')
        transaction.save()
        self.save()
    
    def deposit(self, amount, income_type):
        self.balance = self.balance + amount
        self.total_income = self.total_income + amount
        transaction = TransactionLog.objects.create(wallet=self, amount=amount, transaction_type='deposit', income_type=income_type)
        transaction.save()
        self.save()

    def __str__(self):
        return self.user.user_id

class TransactionLog(models.Model):
    TRANSACTION_TYPE = (
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
    )

    INCOME_TYPE = (
        ('direct', 'Direct'),
        ('step', 'Step'),
        ('binary', 'Binary'),
        ('gift_reward', 'Gift_Reward'),
        ('account', 'Account'),
        ('nil', 'Nil'),
    )

    transaction_id = ShortUUIDField(length=16, max_length=20, prefix="Xe", alphabet="abcdefg1234", primary_key=True)
    wallet = models.ForeignKey(BinaryWallet, on_delete=models.CASCADE, related_name='transaction_log')
    amount = models.FloatField(default=0)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_time = models.DateTimeField(auto_now=True)
    income_type = models.CharField(max_length=20, choices=INCOME_TYPE)
    tag = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.wallet}#{self.transaction_id}"