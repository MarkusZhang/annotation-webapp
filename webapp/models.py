from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200,unique=True,db_index=True)
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    is_labeling_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image_path = models.TextField(unique=True) # shouldn't start with /

class CustomerImage(models.Model):
    product = models.ForeignKey(Product)
    image_path = models.TextField(unique=True) # shouldn't start with /
    # once label_score >=2, this image is confirmed to be correct, once score<=-2, this image is confirmed to be wrong
    label_score = models.IntegerField(default=0)
    times_labeled = models.IntegerField(default=0)

    def is_label_confirmed(self):
        return False
        #TODO: uncomment this line in production
        # return self.label_score <= -2 or self.label_score >= 2

    def reset(self):
        self.label_score = 0
        self.times_labeled = 0

    class Meta:
        ordering = ['pk']

class LabeledBy(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product,null=True) #TODO: remove null=True
    record_time = models.DateTimeField(null=True,blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    num_products_labeled = models.IntegerField(default=0)
    num_images_labeled = models.IntegerField(default=0)
    last_time_label = models.DateTimeField(null=True)

    def reset(self):
        self.num_images_labeled = 0
        self.num_products_labeled = 0
        self.last_time_label = None