from django.db import models
import uuid


# Create your models here.
class Users(models.Model):
    user_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True)
    full_names = models.CharField(max_length=45, null=False, blank=False)
    user_type = models.BooleanField(null=False, blank=False)
    activity = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=45, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, default='+254700000000')
    email = models.CharField(max_length=45, null=True, blank=True)


class Category(models.Model):
    category_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True)
    category_name = models.CharField(max_length=45, null=False, blank=False, unique=True)
    category_description = models.CharField(max_length=10000, null=False, blank=False)


class Pricing(models.Model):
    pricing_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True)
    value = models.CharField(max_length=45, blank=False, null=False)
    commodity = models.CharField(max_length=45, null=False, blank=False)
    description = models.TextField(editable=False, null=False, blank=False)
    category_id = models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE)

    pass


class ProductsAds(models.Model):
    """A class to hold Farmers Ads records."""

    ads_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True)
    pricing_id = models.ForeignKey(Pricing, default=1, verbose_name="pricing", on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, default=1, verbose_name="category", on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, default=1, verbose_name="users", on_delete=models.CASCADE)
    Ads_content = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=256, null=False)
    activity = models.CharField(max_length=256, null=False, blank=False)
    Ads_title = models.CharField(max_length=256, null=False, blank=False)

    @property
    def product_data(self):
        """ Ads computations function """
        return '{} {} {} {}'.format(
            self.ads_id or '',
            self.Ads_content or '',
            self.activity or '',
            self.Ads_title or ''
        )

    def __str__(self):
        return "ProductsAds: {}".format(self.product_data)


class Reviews(models.Model):
    reviews_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True)
    status = models.BooleanField()
    review_message = models.TextField(editable=False, null=False, blank=False)
    date = models.DateField(auto_now=True)
    user_id = models.ForeignKey(Users, verbose_name="user", on_delete=models.CASCADE)
    ads_id = models.ForeignKey(ProductsAds, verbose_name="ads", on_delete=models.CASCADE)
