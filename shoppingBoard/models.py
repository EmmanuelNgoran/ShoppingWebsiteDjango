from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.
# Database design of the shop 
#submitted to change and migration in the future
def image_path(instance , filename):
    return '{}/{}/{}'.format(instance.sub_category.sub_category_name,instance.name,filename)


class Category(models.Model):

    GENDER=(
        ('Male','male'),
        ('Female','female')
    )
    category_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10,choices=GENDER)

    def __str__(self):
        return "{1}-{0}".format(self.category_name,self.gender)
        
    class Meta:
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):

    PRODUCT_TYPE=(('shoes','shoes'),('bottom','bottom'),('top','top'))


    sub_category_name=models.CharField(max_length=30)
    category=models.ForeignKey(Category,related_name='categories', on_delete=models.CASCADE)
   # product_type=models.CharField(choices=PRODUCT_TYPE , max_length=8)
    def __str__(self):
        return "{} {}".format(self.sub_category_name,self.category.gender)
    
    def current_gender(self):
        return "{}".format(self.category.gender)
    current_gender.short_description='gender'
    class Meta:
        verbose_name_plural = 'Sub Categories'

class Inventory(models.Model):

    #size choices
  
    
    DISCOUNT=(
        ('20','low'),
        ('30','midrange'),
        ('50','medium'),
        ('70','super')
    )
    name=models.CharField(max_length=50,default='product')
    sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    unit_price=models.PositiveIntegerField()
    discount=models.CharField(max_length=2, choices=DISCOUNT,null=True)
    description=models.TextField(max_length=500)
    #image field to be added
    image1=models.ImageField(upload_to=image_path)
    image2=models.ImageField(upload_to=image_path)
    image3=models.ImageField(upload_to=image_path)
    brand=models.CharField(max_length=50)
    published_on=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_photo(self):
        return mark_safe('<a href="{0}"><img src="{0}" width="150" /></a>'.format(self.image1.url ))
    get_photo.short_description = "Preview"
    get_photo.allow_tags = True

    class Meta:
        verbose_name_plural = 'Products'
    
class productSpec(models.Model):

    SIZE_TOP_CLOTH=('TOP CLOTH',(('XS','extra small'),
        ('S','small'),
        ('L','large'),
        ('M','medium'),
        ('XL','extra large')))

    SIZE_BOTTOM_CLOTH= ('BOTTOM CLOTH',( ('26','26'),
        ('28','28'),
        ('30','30'),
        ('32','32'),
        ('34','34'),
        ('36','36')))

    SIZE_SHOES= ('SHOES', (('3','3'),
        ('4','4'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'))) 
    
    SIZE=(SIZE_BOTTOM_CLOTH,SIZE_SHOES,SIZE_TOP_CLOTH)

    

    quantity=models.PositiveIntegerField()
    size=models.CharField( max_length=2,
        choices=SIZE,
        )
    product=models.ForeignKey(Inventory,related_name='product_spec',on_delete=models.CASCADE)
    color=models.CharField(max_length=10)
   

    def productName(self):
        return "{}".format(self.product.name)
    product.short_description='Product name'


class Order(models.Model):
    address=models.TextField(max_length=300)
    phone_number=models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    def productName(self):
        return "{}".format(self.user.username)
    user.short_description='customer name'

    def __str__(self):
        return self.user.username

class OrderItems(models.Model):
    order=models.ForeignKey(Order,related_name='from_order',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    ship_date=models.DateField(null=True)
    product=models.ForeignKey(Inventory,related_name='products',on_delete=models.CASCADE)
    shipping_charge=models.PositiveIntegerField()
    price=models.PositiveIntegerField(default=1)
    size=models.CharField(max_length=2,null=True)

    class Meta:
        verbose_name_plural = 'Items Ordered'

    def __str__(self):
        return "order by {} and shipped on {}".format(self.order.user.username,self.ship_date)
    def get_photo(self):
        return mark_safe('<a href="{0}"><img src="{0}" width="150" /></a>'.format(self.product.image1.url ))
    get_photo.short_description = "Preview"
    get_photo.allow_tags = True

   
#user data can belong to only one user


   

